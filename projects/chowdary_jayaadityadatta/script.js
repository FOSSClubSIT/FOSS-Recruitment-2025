const API_KEY = "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"; // PASTE YOUR GROQ API KEY HERE
const API_URL = `https://api.groq.com/openai/v1/chat/completions`;

// Get references to our HTML elements
const headlineInput = document.getElementById('headlineInput');
const aboutInput = document.getElementById('aboutInput');
const analyzeBtn = document.getElementById('analyzeBtn');
const resultsSection = document.getElementById('resultsSection');

// Main function to call the Groq API
async function getAIFeedback(headline, about) {
    const prompt = `
        Analyze the following LinkedIn profile sections for a college student. Provide actionable feedback.
        The feedback should be concise, constructive, and use bullet points.
        Format the entire output in HTML (use <strong> for headings and <ul> and <li> for lists).

        **Headline:** "${headline}"
        **About Summary:** "${about}"

        Start your analysis with "<h3>Analysis Results:</h3>".
    `;

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${API_KEY}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                "model": "llama3-8b-8192",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            })
        });

        if (!response.ok) {
            const errorBody = await response.text();
            console.error("API Error Body:", errorBody);
            throw new Error(`API request failed with status ${response.status}`);
        }

        const data = await response.json();
        const feedback = data.choices[0].message.content;
        return feedback;

    } catch (error) {
        console.error("Error fetching AI feedback:", error);
        return "<p>Sorry, something went wrong. The API request failed. Please check the console for a detailed error message.</p>";
    }
}


// Set up the event listener for the button
analyzeBtn.addEventListener('click', async () => {
    const headline = headlineInput.value;
    const about = aboutInput.value;

    if (!headline || !about) {
        resultsSection.innerHTML = "<p>Please paste both your headline and about summary before analyzing.</p>";
        return;
    }

    // --- UI Update: Start Loading ---
    analyzeBtn.disabled = true;
    resultsSection.innerHTML = '<div class="loader"></div><p>🤖 Analyzing your profile... this can take a moment.</p>';

    // Get the feedback from the AI
    const feedbackHtml = await getAIFeedback(headline, about);

    // --- UI Update: Stop Loading ---
    resultsSection.innerHTML = feedbackHtml;
    analyzeBtn.disabled = false;
});