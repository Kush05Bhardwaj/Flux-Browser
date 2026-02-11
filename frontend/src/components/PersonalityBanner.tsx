// PersonalityBanner component

interface PersonalityBannerProps {
  message: string;
}

export default function PersonalityBanner({message}: PersonalityBannerProps) {
    return (
        <div className = "bg-pink-200 text-pink-900 p-4 rounded-xl shadow-md mb-6 text-center font-semibold">
            {message}
        </div>
    );
}
