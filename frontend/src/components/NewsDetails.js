import React from "react";
import cnbcIcon from "./icons/cnbc.webp";
import bloombergIcon from "./icons/bloomberg.png";
import foxBusinessIcon from "./icons/foxbusiness.png";

// Helper object to map sources to icons
const icons = {
  CNBC: cnbcIcon,
  Bloomberg: bloombergIcon,
  "Fox Business": foxBusinessIcon,
};

const NewsDetail = ({ newsArticle }) => {
  const { source, title, url, date } = newsArticle;
  const iconSrc = icons[source] || ""; // Default to empty string or a default icon if source is not recognized

  const formatDate = (dateString) => {
    if (!dateString) return "Null";
    const options = {
      year: "numeric",
      month: "long",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    };
    return new Date(dateString).toLocaleDateString("en-US", options);
  };

  return (
    <div className="flex flex-col w-full border-b border-gray-200 py-4">
      <h2 className="flex items-center space-x-2 text-xl font-semibold text-gray-900">
        {iconSrc && (
          <img src={iconSrc} alt={`${source} icon`} className="w-6 h-6" />
        )}
        <a href={url} className="hover:text-blue-600 transition-colors">
          {title}
        </a>
      </h2>
      <p className="text-gray-500 mt-1">Date: {formatDate(date)}</p>
    </div>
  );
};

export default NewsDetail;
