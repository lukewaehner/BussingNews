import { useEffect, useState } from "react";

import NewsDetails from "../components/NewsDetails";

const Home = () => {
  const [news, setNews] = useState(null); // Initialize news as an empty array

  useEffect(() => {
    const fetchNews = async () => {
      const response = await fetch("/api/news");
      const json = await response.json();

      if (response.ok) {
        setNews(json.newsArticles);
      }
    };

    fetchNews();
  }, []);

  console.log(news);

  return (
    <div className="home">
      <div className="news">
        {news &&
          news.map((newsArticle) => (
            <NewsDetails key={newsArticle.id} newsArticle={newsArticle} />
          ))}
      </div>
    </div>
  );
};

export default Home;
