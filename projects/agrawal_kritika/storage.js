// Simple shared storage for mood entries
// Each entry: { date: "YYYY-MM-DD", mood: "happy", note: "..." }

var STORAGE_KEY = "mood_journal_entries_v1";

var Storage = {
  _readAll: function () {
    try {
      const data = localStorage.getItem(STORAGE_KEY);
      return data ? JSON.parse(data) : {};
    } catch (error) {
      console.error('Error reading from localStorage:', error);
      return {};
    }
  },

  _writeAll: function (map) {
    try {
      if (!map || typeof map !== 'object') {
        throw new Error('Invalid data format');
      }
      localStorage.setItem(STORAGE_KEY, JSON.stringify(map));
      return true;
    } catch (error) {
      console.error('Error writing to localStorage:', error);
      return false;
    }
  },

  getEntry: function (date) {
    if (!date || typeof date !== 'string') {
      console.warn('Invalid date provided to getEntry:', date);
      return null;
    }
    
    try {
      const data = this._readAll();
      return data[date] || null;
    } catch (error) {
      console.error('Error getting entry:', error);
      return null;
    }
  },

  saveEntry: function (entry) {
    if (!entry || !entry.date || typeof entry.date !== 'string') {
      console.warn('Invalid entry provided to saveEntry:', entry);
      return false;
    }
    
    try {
      var map = this._readAll();
      map[entry.date] = { ...map[entry.date], ...entry };
      return this._writeAll(map);
    } catch (error) {
      console.error('Error saving entry:', error);
      return false;
    }
  }
};

window.Storage = Storage;