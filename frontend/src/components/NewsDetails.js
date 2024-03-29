const NewsDetail = ({ newsArticle }) => {
  return (
    <div className="news-detail">
      <h2 className="news-title">
        <a href={newsArticle.url}>{newsArticle.title}</a>
      </h2>
      <p className="news-time">{newsArticle.date}</p>
    </div>
  );
};

export default NewsDetail;
