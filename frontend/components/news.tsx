"use client";

import React from "react";
import useSWR from "swr";

interface NewsItem {
  _id: string;
  title: string;
}

const fetcher = (url: string): Promise<NewsItem[]> =>
  fetch(url).then((res) => res.json());

export default function News() {
  const { data, error } = useSWR<NewsItem[]>("/api/news", fetcher);
  console.log(data, error);
  if (error) return <div>Failed to load</div>;
  if (!data) return <div>Loading...</div>;

  return (
    <div className="text-center space-y-5 mt-8">
      <h2 className="text-7xl uppercase">News</h2>
      <ul className="space-y-3">
        {data.map((newsItem: NewsItem) => (
          <li key={newsItem._id}>{newsItem.title}</li>
        ))}
      </ul>
    </div>
  );
}
