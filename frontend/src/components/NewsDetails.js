const NewsDetail = ({ newsArticle }) => {
  return (
    <div className="news-detail">
      <h2>{newsArticle.title}</h2>
      <p>
        {" "}
        <italic>{newsArticle.url}</italic>
      </p>
      <p>{newsArticle.createdAt}</p>
    </div>
  );
};

export default NewsDetail;
