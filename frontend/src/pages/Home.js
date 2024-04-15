import { useEffect, useState } from "react";
import NewsDetails from "../components/NewsDetails";

const Home = () => {
  const [news, setNews] = useState([]);
  const [sourceIndex, setSourceIndex] = useState(-1);
  const [sources, setSources] = useState([]);
  const [dateSortDirection, setDateSortDirection] = useState(null);

  useEffect(() => {
    const fetchNews = async () => {
      const response = await fetch("/api/news");
      const json = await response.json();
      if (response.ok) {
        setNews(json.newsArticles);
        extractSources(json.newsArticles);
      }
    };

    fetchNews();
  }, []);

  const extractSources = (newsArticles) => {
    const uniqueSources = [
      "All",
      ...new Set(newsArticles.map((article) => article.source)),
    ];
    setSources(uniqueSources);
  };

  const cycleSources = () => {
    setSourceIndex((prevIndex) => (prevIndex + 1) % sources.length);
  };

  const toggleDateSort = () => {
    setDateSortDirection((prevDirection) =>
      prevDirection === "ascending" ? "descending" : "ascending"
    );
  };

  const sortedAndFilteredNews = () => {
    let filteredNews =
      sourceIndex >= 0 && sources[sourceIndex] !== "All"
        ? news.filter((article) => article.source === sources[sourceIndex])
        : news;

    if (dateSortDirection) {
      filteredNews = filteredNews.sort((a, b) => {
        const dateA = new Date(a.date);
        const dateB = new Date(b.date);
        return dateSortDirection === "ascending"
          ? dateA - dateB
          : dateB - dateA;
      });
    }

    return filteredNews;
  };

  return (
    <div className="home">
      <div className="flex gap-5 mb-4">
        <button
          onClick={cycleSources}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition ease-in-out duration-300"
        >
          Sort by Source:{" "}
          {sources.length > 0 && sourceIndex >= 0
            ? sources[sourceIndex]
            : "None"}
        </button>
        <button
          onClick={toggleDateSort}
          className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded transition ease-in-out duration-300"
        >
          Sort by Date{" "}
          {dateSortDirection
            ? dateSortDirection === "ascending"
              ? "↓"
              : "↑"
            : ""}
        </button>
      </div>
      <div className="news">
        {sortedAndFilteredNews().map((newsArticle) => (
          <NewsDetails key={newsArticle.id} newsArticle={newsArticle} />
        ))}
      </div>
    </div>
  );
};

export default Home;
