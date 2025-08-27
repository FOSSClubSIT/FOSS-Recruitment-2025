// Mood Quotes
const quotes = {
  happy: { text: "Happiness is contagious — keep spreading your joy!", color: "#FFF9C4" },
  sad: { text: "Even the darkest clouds eventually clear. Stay hopeful.", color: "#E1F5FE" },
  angry: { text: "Channel your anger into something productive, not destructive.", color: "#FFCDD2" },
  calm: { text: "Your calm is a superpower. Breathe and embrace it.", color: "#C8E6C9" },
  excited: { text: "Your excitement fuels your creativity — let it shine!", color: "#FFE082" },
  tired: { text: "Rest is progress. Recharge and face tomorrow stronger.", color: "#D7CCC8" },
  anxious: { text: "Step by step. You've overcome every challenge before, you can now.", color: "#B3E5FC" },
  confident: { text: "Believe in yourself. You are capable of amazing things.", color: "#D1C4E9" },
  bored: { text: "Try something new today; even small changes spark growth.", color: "#EEEEEE" },
  "in-love": { text: "Love deeply and openly; it enriches life in countless ways.", color: "#F8BBD0" }
};

// Use local date instead of UTC to avoid timezone issues
function getTodayKey() {
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, '0');
  const day = String(now.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

const todayKey = getTodayKey();

function applyMoodUI(mood) {
  if (!mood) return;
  
  // Clear previous selections and select new one
  document.querySelectorAll('.emoji').forEach(emoji => emoji.classList.remove('selected'));
  const selectedEmoji = document.querySelector(`[data-mood="${mood}"]`);
  if (selectedEmoji) selectedEmoji.classList.add('selected');
  
  // Apply quote and background
  const q = quotes[mood];
  if (q) {
    document.body.style.background = q.color;
    const quoteEl = document.getElementById('quote');
    if (quoteEl) {
      quoteEl.innerHTML = `<span class="highlight">${mood.replace('-', ' ')}</span>: ${q.text}`;
      quoteEl.style.display = 'block';
    }
  }
}

function showSaveFeedback(success = true) {
  const saveBtn = document.getElementById('save-note');
  if (!saveBtn) return;
  
  const originalText = saveBtn.textContent;
  const originalBackground = saveBtn.style.background;
  
  saveBtn.textContent = success ? 'Saved!' : 'Error!';
  saveBtn.style.background = success ? 
    'linear-gradient(180deg, #10b981, #059669)' : 
    'linear-gradient(180deg, #ef4444, #dc2626)';
  
  setTimeout(() => {
    saveBtn.textContent = originalText;
    saveBtn.style.background = originalBackground || 'linear-gradient(180deg, #3b82f6, #2563eb)';
  }, 2000);
}

function saveEntry(data) {
  try {
    const existing = Storage.getEntry(todayKey) || { date: todayKey };
    Storage.saveEntry({ ...existing, ...data });
    window.dispatchEvent(new CustomEvent('moodUpdated', { detail: { date: todayKey, ...data } }));
    return true;
  } catch (error) {
    console.error('Error saving entry:', error);
    return false;
  }
}

function initIndexPage() {
  const moodCells = document.querySelectorAll('.emoji');
  if (!moodCells.length) return;

  // Restore existing mood & note
  const entry = Storage.getEntry(todayKey);
  if (entry?.mood) applyMoodUI(entry.mood);
  
  const noteInput = document.getElementById('note-input');
  if (noteInput && entry?.note) noteInput.value = entry.note;

  // Add mood selection events
  moodCells.forEach(emoji => {
    emoji.addEventListener('click', () => {
      const mood = emoji.getAttribute('data-mood');
      applyMoodUI(mood);
      saveEntry({ mood });
    });
  });

  // Add save note event
  const saveBtn = document.getElementById('save-note');
  if (saveBtn) {
    saveBtn.addEventListener('click', () => {
      const noteInput = document.getElementById('note-input');
      const noteVal = noteInput ? noteInput.value || '' : '';
      const success = saveEntry({ note: noteVal });
      showSaveFeedback(success);
    });
  }

  // Add enter key support
  const noteInputEl = document.getElementById('note-input');
  if (noteInputEl) {
    noteInputEl.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') document.getElementById('save-note').click();
    });
  }
}

document.addEventListener('DOMContentLoaded', initIndexPage);
