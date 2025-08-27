var MOOD_TO_EMOJI = {
  happy: "😊", sad: "😢", angry: "😠", calm: "😌", excited: "🤩",
  tired: "🥱", anxious: "😰", confident: "😎", bored: "😐", "in-love": "😍"
};

var activeYear, activeMonth;

function formatMonthLabel(y, m) {
  return new Date(y, m, 1).toLocaleString(undefined, { month: "long", year: "numeric" });
}

function keyFromDate(d) {
  // Use local date formatting to avoid timezone issues
  const year = d.getFullYear();
  const month = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

function renderDayCell(date, otherMonth) {
  var key = keyFromDate(date);
  var entry = Storage.getEntry(key);
  var isToday = key === keyFromDate(new Date());
  var moodEmoji = entry?.mood ? MOOD_TO_EMOJI[entry.mood] : "";

  var classes = "day";
  if (otherMonth) classes += " other-month";
  if (isToday) classes += " today";
  if (entry?.mood) classes += " has-entry";

  return `<div class="${classes}" data-key="${key}">
            <div class="date">${date.getDate()}</div>
            <div class="emoji-cell">${moodEmoji}</div>
          </div>`;
}

function buildCalendarDays(year, month) {
  var start = new Date(year, month, 1);
  var end = new Date(year, month + 1, 0);
  var startWeekday = (start.getDay() + 6) % 7;
  var totalDays = end.getDate();
  var cells = [];

  // Week headers
  ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"].forEach(d => {
    cells.push(`<div class="weekday">${d}</div>`);
  });

  // Leading blanks
  for (var i = 0; i < startWeekday; i++) {
    var d = new Date(year, month, i - startWeekday + 1);
    cells.push(renderDayCell(d, true));
  }

  // Actual days
  for (var day = 1; day <= totalDays; day++) {
    cells.push(renderDayCell(new Date(year, month, day), false));
  }

  // Trailing blanks
  var remainder = (cells.length - 7) % 7;
  if (remainder) {
    var last = new Date(year, month, totalDays);
    for (var j = 1; j <= 7 - remainder; j++) {
      var d3 = new Date(last);
      d3.setDate(last.getDate() + j);
      cells.push(renderDayCell(d3, true));
    }
  }
  return cells.join("");
}

function showEntryDetails(key) {
  var entry = Storage.getEntry(key);
  if (!entry) return;
  
  var date = new Date(key);
  var dateStr = date.toLocaleDateString(undefined, { 
    weekday: 'long', 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
  });
  
  var moodText = entry.mood ? entry.mood.replace('-', ' ') : 'No mood recorded';
  var noteText = entry.note || 'No note added';
  
  var details = `
    <div class="entry-details card">
      <h3>${dateStr}</h3>
      <div class="entry-mood">
        <strong>Mood:</strong> ${moodText} ${entry.mood ? MOOD_TO_EMOJI[entry.mood] : ''}
      </div>
      <div class="entry-note">
        <strong>Note:</strong> ${noteText}
      </div>
    </div>
  `;
  
  // Remove existing details and add new ones
  var existing = document.querySelector('.entry-details');
  if (existing) existing.remove();
  
  document.querySelector('.container').insertAdjacentHTML('beforeend', details);
}

function drawCalendar() {
  document.getElementById("month-label").textContent = formatMonthLabel(activeYear, activeMonth);
  document.getElementById("calendar-grid").innerHTML = buildCalendarDays(activeYear, activeMonth);
  
  // Add click events to days
  document.querySelectorAll('.day').forEach(day => {
    day.addEventListener('click', function() {
      var key = this.getAttribute('data-key');
      if (key) showEntryDetails(key);
    });
  });
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
  };
}

document.addEventListener("DOMContentLoaded", function () {
  var t = new Date();
  activeYear = t.getFullYear();
  activeMonth = t.getMonth();
  drawCalendar();
  wireEvents();
  
  // Listen for mood updates from the main page
  window.addEventListener('moodUpdated', function() {
    setTimeout(drawCalendar, 100);
  });
});