// ResultCard component

import StatsBar from "./StatsBar";

interface ResultCardProps {
  result: {
    url: string;
    title?: string;
    stats: {
      clarity: number;
      depth: number;
      credibility: number;
      freshness: number;
    };
  };
}

export default function ResultCard({ result }: ResultCardProps) {
    return (
        <div className="bg-white p-6 rounded-2xl shadow-lg mb-4 hover:scale-105 transition-transform duration-300 border border-purple-200">
            <a href = {result.url} target="_blank" rel="noopener noreferrer" className="text-xl font-bold text-purple-700 hover:underline">
                {result.title || result.url}
            </a>
            <div className="mt-4">
                <StatsBar label="Clarity" value={result.stats.clarity} />
                <StatsBar label="Depth" value={result.stats.depth} />
                <StatsBar label="Credibility" value={result.stats.credibility} />
                <StatsBar label="Freshness" value={result.stats.freshness} />
            </div>
        </div>
    );
}