import { useEffect, useState } from "react";

const Home = () => {
  const [news, setNews] = useState(null);

  useEffect(() => {
    const fetchNews = async () => {
      const response = await fetch("http://localhost:4000/api/news");
      const json = await response.json();

      if (response.ok) {
        setNews(json);
      }
    };

    fetchNews();
  }, []);
  return (
    <div className="home">
      <div className="news">
        {news &&
          news.map((newsart) => <p key={newsart._id}>{newsart.title}</p>)}
      </div>
    </div>
  );
};

export default Home;
