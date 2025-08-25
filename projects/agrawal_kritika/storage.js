// Simple shared storage for mood entries
// Each entry: { date: "YYYY-MM-DD", mood: "happy", note: "..." }

var STORAGE_KEY = "mood_journal_entries_v1";

var Storage = {
  _readAll: function () {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return {};
      var data = JSON.parse(raw);
      if (typeof data === "object" && data) return data;
      return {};
    } catch (e) {
      return {};
    }
  },

  _writeAll: function (map) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(map));
  },

  getEntry: function (date) {
    var map = this._readAll();
    return map[date] || null;
  },

  saveEntry: function (entry) {
    if (!entry || !entry.date) return;
    var map = this._readAll();
    if (!map[entry.date]) map[entry.date] = {};
    Object.assign(map[entry.date], entry);
    this._writeAll(map);
  },

  getAllEntries: function () {
    var map = this._readAll();
    var keys = Object.keys(map).sort();
    var arr = [];
    for (var i = 0; i < keys.length; i++) {
      arr.push(map[keys[i]]);
    }
    return arr;
  },

  getCounts: function () {
    var counts = {};
    var all = this.getAllEntries();
    for (var i = 0; i < all.length; i++) {
      var e = all[i];
      if (!e.mood) continue;
      if (!counts[e.mood]) counts[e.mood] = 0;
      counts[e.mood]++;
    }
    return counts;
  },

  getMostCommonMood: function () {
    var counts = this.getCounts();
    var topMood = null;
    var topCount = 0;
    for (var m in counts) {
      if (counts[m] > topCount) {
        topMood = m;
        topCount = counts[m];
      }
    }
    return { mood: topMood, count: topCount };
  },

  getCurrentStreak: function () {
    var map = this._readAll();
    var streak = 0;
    var today = new Date();

    while (true) {
      var d = new Date();
      d.setDate(today.getDate() - streak);
      var key = d.getFullYear() + "-" +
        String(d.getMonth() + 1).padStart(2, "0") + "-" +
        String(d.getDate()).padStart(2, "0");

      var e = map[key];
      if (e && e.mood) streak++;
      else break;
    }
    return streak;
  }
};

window.Storage = Storage;
