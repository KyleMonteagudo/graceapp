import React, { useState } from 'react';
import './index.css';


function App() {
  const [input, setInput] = useState('');
  const [chatHistory, setChatHistory] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    try {
      const res = await fetch(process.env.REACT_APP_API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: input })
      });

      const data = await res.json();
      const message = data.choices[0].message.content;

      setChatHistory(prev => [...prev, { question: input, answer: message }]);
      setInput('');
    } catch (error) {
      console.error('Error fetching chatbot response:', error);
      setChatHistory(prev => [...prev, { question: input, answer: 'Error fetching response.' }]);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Test Azure OpenAI Chat</h1>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask a question..."
          />
          <button type="submit">Send</button>
        </form>
        <p style={{ marginTop: '1rem' }}>
          I'm here to answer questions feel free to ask away!
        </p>

        <div className="chat-container">
          {chatHistory.map((entry, index) => (
            <div key={index} className="chat-entry">
              <div className="user-question"><strong>You:</strong> {entry.question}</div>
              <div className="response-box">{entry.answer}</div>
            </div>
          ))}
        </div>
      </header>
    </div>
  );
}

export default App;
