// Home page component

import { useState } from "react";
import SearchBar from "../components/SearchBar";
import ResultCard from "../components/ResultCard";
import PersonalityBanner from "../components/PersonalityBanner";

interface SearchResult {
  url: string;
  stats: {
    clarity: number;
    depth: number;
    credibility: number;
    freshness: number;
  };
}

interface SearchResponse {
  results: SearchResult[];
  message: string;
}

export default function Home() {
    const [results, setResults] = useState<SearchResult[]>([]);
    const [message, setMessage] = useState("Welcome to Flux Browser! Activate your Arc to see results.");

    const searchFlux = async (query: string) => {
        setMessage("Activating Arc...");
        try {
            const response = await fetch("http://localhost:8000/search?q=" + encodeURIComponent(query));
            const data: SearchResponse = await response.json();
            setResults(data.results);
            setMessage(data.message);
        } catch (error) {
            setMessage("Error activating Arc. Please try again.");
            console.error("Search error:", error);
        }
    };

    return (
        <div className="min-h-screen bg-gradient-to-br from-pink-100 via-purple-100 to-indigo-200 p-10">
        <h1 className="text-5xl font-extrabold text-center text-purple-700 mb-10">
            {message}
        </h1>
            <SearchBar onSearch={searchFlux} />
            {message && <PersonalityBanner message={message} />}
            
        {results.map((r, i) => (
        <ResultCard key={i} result={r} />
      ))}
    </div>
  );
}