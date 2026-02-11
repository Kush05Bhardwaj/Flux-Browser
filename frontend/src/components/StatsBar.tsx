// StatsBar component

interface StatsBarProps {
  label: string;
  value: number;
}

export default function StatsBar({ label, value }: StatsBarProps) {
  return (
    <div className="mb-2">
      <div className="flex justify-between text-sm">
        <span>{label}</span>
        <span>{value}/5</span>
      </div>
      <div className="w-full bg-gray-200 h-2 rounded">
        <div
          className="bg-purple-500 h-2 rounded transition-all duration-500"
          style={{ width: `${value * 20}%` }}
        ></div>
      </div>
    </div>
  );
}