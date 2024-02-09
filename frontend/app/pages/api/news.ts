// pages/api/news.ts
import type { NextApiRequest, NextApiResponse } from "next";

type NewsItem = {
  id: string;
  title: string;
};

type Data = {
  news: NewsItem[];
};

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
  const exampleNewsData: NewsItem[] = [{ id: "1", title: "First news item" }];

  res.status(200).json({ news: exampleNewsData });
}
