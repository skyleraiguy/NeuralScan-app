import React, { useState } from 'react';
import Header from './components/Header';
import DataInput from './components/DataInput';
import Results from './components/Results';

export function App() {
    const [results, setResults] = useState(null);

    return (
        <div className="App">
            <Header />
            <DataInput setResults={setResults} />
            {results && <Results results={results} />}
        </div>
    );
}
