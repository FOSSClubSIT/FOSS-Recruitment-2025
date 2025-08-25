var MOOD_TO_EMOJI = {
  happy: "😊", sad: "😢", angry: "😠", calm: "😌", excited: "🤩",
  tired: "🥱", anxious: "😰", confident: "😎", bored: "😐", "in-love": "😍"
};

var activeYear;
var activeMonth; // 0-based
var selectedDateKey;

function formatMonthLabel(y, m) {
  var d = new Date(y, m, 1);
  return d.toLocaleString(undefined, { month: "long", year: "numeric" });
}

function keyFromDate(d) {
  var y = d.getFullYear();
  var m = String(d.getMonth() + 1).padStart(2, "0");
  var day = String(d.getDate()).padStart(2, "0");
  return y + "-" + m + "-" + day;
}

function renderDayCell(date, otherMonth) {
  var key = keyFromDate(date);
  var entry = Storage.getEntry(key);
  var isToday = (key === keyFromDate(new Date()));
  var moodEmoji = entry && entry.mood ? MOOD_TO_EMOJI[entry.mood] : "";
  var classes = "day";
  if (otherMonth) classes += " other-month";
  if (isToday) classes += " today";

  return '<div class="' + classes + '" data-key="' + key + '">' +
    '<div class="date">' + date.getDate() + '</div>' +
    '<div class="emoji-cell">' + moodEmoji + '</div>' +
    "</div>";
}

function buildCalendarDays(year, month) {
  var start = new Date(year, month, 1);
  var end = new Date(year, month + 1, 0);
  var startWeekday = (start.getDay() + 6) % 7; // Monday=0
  var totalDays = end.getDate();

  var cells = [];

  // Weekday header
  var weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
  for (var i = 0; i < weekdays.length; i++) {
    cells.push('<div class="weekday">' + weekdays[i] + "</div>");
  }

  // Leading blanks
  for (var i = 0; i < startWeekday; i++) {
    var d = new Date(year, month, i - startWeekday + 1);
    cells.push(renderDayCell(d, true));
  }

  // Actual days
  for (var day = 1; day <= totalDays; day++) {
    var d2 = new Date(year, month, day);
    cells.push(renderDayCell(d2, false));
  }

  // Fill end of grid
  var totalCellsExcludingHeader = cells.length - 7;
  var remainder = totalCellsExcludingHeader % 7;
  if (remainder !== 0) {
    var toAdd = 7 - remainder;
    var last = new Date(year, month, totalDays);
    for (var j = 1; j <= toAdd; j++) {
      var d3 = new Date(last);
      d3.setDate(last.getDate() + j);
      cells.push(renderDayCell(d3, true));
    }
  }
  return cells.join("");
}

function drawCalendar() {
  document.getElementById("month-label").textContent = formatMonthLabel(activeYear, activeMonth);
  document.getElementById("calendar-grid").innerHTML = buildCalendarDays(activeYear, activeMonth);
}

function selectDate(key) {
  selectedDateKey = key;
  // View-only mode: no editing here
}

function wireEvents() {
  document.getElementById("prev-month").onclick = function () {
    var d = new Date(activeYear, activeMonth - 1, 1);
    activeYear = d.getFullYear();
    activeMonth = d.getMonth();
    drawCalendar();
  };

  document.getElementById("next-month").onclick = function () {
    var d = new Date(activeYear, activeMonth + 1, 1);
    activeYear = d.getFullYear();
    activeMonth = d.getMonth();
    drawCalendar();
  };

  document.getElementById("today-btn").onclick = function () {
    var t = new Date();
    activeYear = t.getFullYear();
    activeMonth = t.getMonth();
    drawCalendar();
    selectDate(keyFromDate(t));
  };

  document.getElementById("calendar-grid").onclick = function (e) {
    var day = e.target.closest(".day");
    if (!day) return;
    var key = day.getAttribute("data-key");
    if (key) selectDate(key);
  };
}

document.addEventListener("DOMContentLoaded", function () {
  var t = new Date();
  activeYear = t.getFullYear();
  activeMonth = t.getMonth();
  drawCalendar();
  wireEvents();
  selectDate(keyFromDate(t));
});
