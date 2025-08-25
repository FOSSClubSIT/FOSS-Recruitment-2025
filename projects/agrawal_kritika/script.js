// Mood Quotes
const quotes = {
  happy: { text: "Happiness is contagious — keep spreading your joy!", color: "#FFF9C4" },
  sad: { text: "Even the darkest clouds eventually clear. Stay hopeful.", color: "#E1F5FE" },
  angry: { text: "Channel your anger into something productive, not destructive.", color: "#FFCDD2" },
  calm: { text: "Your calm is a superpower. Breathe and embrace it.", color: "#C8E6C9" },
  excited: { text: "Your excitement fuels your creativity — let it shine!", color: "#FFE082" },
  tired: { text: "Rest is progress. Recharge and face tomorrow stronger.", color: "#D7CCC8" },
};

document.querySelectorAll('.emoji').forEach(emoji => {
  emoji.addEventListener('click', () => {
    const mood = emoji.getAttribute('data-mood');
    const quote = quotes[mood];

    // Change background
    document.body.style.background = quote.color;
    
    // Show quote
    document.getElementById('quote').innerHTML = 
      `<span class="highlight">${mood.replace('-', ' ')}</span>: ${quote.text}`;
  });
});