// pages/index.tsx
import React from "react";
import News from "@/components/news"; // Import your component

export default function Home() {
  return (
    <main className="flex flex-col items-center">
      <News />
    </main>
  );
}
