const categories = [
    { name: "Food", keywords: ["zomato", "swiggy", "blinkit", "domino", "kfc", "pizza"] },
    { name: "Shopping", keywords: ["amazon", "flipkart", "myntra", "ajio", "meesho"] },
    { name: "Travel", keywords: ["ola", "uber", "irctc", "airasia", "makemytrip"] },
    { name: "Bills", keywords: ["electricity", "dth", "broadband", "gas", "prepaid", "postpaid"] }
];

const categoryColors = {
    "Food": "#27ae60",      // green
    "Shopping": "#e67e22",  // orange
    "Travel": "#9b59b6",    // purple
    "Bills": "#c0392b",     // red
    "Other": "#7f8c8d"      // gray
};


let expenses = JSON.parse(localStorage.getItem("expenses")) || [];
let total = expenses.reduce((sum, e) => sum + e.amount, 0);

const smsInput = document.getElementById("sms");
const addBtn = document.getElementById("addBtn");
const clearBtn = document.getElementById("clearBtn");
const copyAllBtn = document.getElementById("copyAll");
const list = document.getElementById("list");
const totalEl = document.getElementById("total");
const catTableBody = document.querySelector("#catTable tbody");

// Detect category from SMS
function detectCategory(text) {
    text = text.toLowerCase();
    for (let c of categories) {
        if (c.keywords.some(k => text.includes(k))) return c.name;
    }
    return "Other";
}

// Extract date from SMS
function extractDate(text) {
    const dmy = text.match(/\b(\d{2})[-\/](\d{2})[-\/](\d{4})\b/);
    if (dmy) return `${dmy[3]}-${dmy[2]}-${dmy[1]}`;
    const ymd = text.match(/\b(20\d{2})[-\/](\d{2})[-\/](\d{2})\b/);
    if (ymd) return `${ymd[1]}-${ymd[2]}-${ymd[3]}`;
    return new Date().toISOString().slice(0, 10);
}

// Render list
function render() {
    totalEl.innerText = total.toFixed(2);

    // Render expenses list
    list.innerHTML = "";
    [...expenses].reverse().forEach(e => {  // most recent first
        let li = document.createElement("li");
        li.style.borderLeft = `6px solid ${categoryColors[e.category] || "#000"}`; // color strip
        li.innerHTML = `<span class="cat" style="color:${categoryColors[e.category] || "#000"}">${e.category}</span> ₹${e.amount.toFixed(2)} <span class="date">${e.date}</span><br>${e.sms}`;
        list.appendChild(li);
    });

    // Render category totals
    const catTotals = {};
    expenses.forEach(e => {
        catTotals[e.category] = (catTotals[e.category] || 0) + e.amount;
    });

    catTableBody.innerHTML = "";
    for (let [cat, amt] of Object.entries(catTotals)) {
        const tr = document.createElement("tr");
        tr.style.backgroundColor = categoryColors[cat] + "20"; // light transparent color for row
        tr.innerHTML = `<td style="color:${categoryColors[cat]}">${cat}</td><td>₹${amt.toFixed(2)}</td>`;
        catTableBody.appendChild(tr);
    }

}

// Add expense
function addExpense() {
    const sms = smsInput.value.trim();
    if (!sms) return alert("Please paste SMS!");
    const match = sms.match(/(?:INR|Rs\.?|₹)\s?(\d+(\.\d{1,2})?)/i);
    if (!match) return alert("No amount found in SMS!");
    const amt = parseFloat(match[1]);
    const category = detectCategory(sms);
    const date = extractDate(sms);
    expenses.push({ amount: amt, sms, category, date });
    total += amt;
    localStorage.setItem("expenses", JSON.stringify(expenses));
    render();
    smsInput.value = "";
}

// Clear all
function clearAll() {
    if (confirm("Clear all expenses?")) {
        expenses = [];
        total = 0;
        localStorage.removeItem("expenses");
        render();
    }
}

// Copy all expenses
function copyAll() {
    if (expenses.length === 0) return alert("No expenses to copy!");
    const text = expenses.map(e => `${e.date} | ${e.category} | ₹${e.amount.toFixed(2)} | ${e.sms}`).join("\n");
    navigator.clipboard.writeText(text);
    alert("All expenses copied!");
}

// Event listeners
addBtn.addEventListener("click", addExpense);
clearBtn.addEventListener("click", clearAll);
copyAllBtn.addEventListener("click", copyAll);

// Initial render
render();
