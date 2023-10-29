import React, { useState } from "react";
import axios from "axios";

export const DataInput = ({ setResults }) => {
    const [data, setData] = useState('');

    const analyzeData = async () => {
        try {
            // Replace with your backend API endpoint
            const apiUrl = 'https://big-pig-huge.ngrok-free.app ';

            // POST request to the backend
            const response = await axios.post(apiUrl, { data });

            // Set the results in the parent component
            setResults(response.data.result);

        } catch (error) {
            console.error('An error occurred:', error);
        }
    };

    return (
        <div>
            <h2>Input MEG Data</h2>
            <textarea value={data} onChange={(e) => setData(e.target.value)} />
            <button onClick={analyzeData}>Analyze</button>
        </div>
    );
};
