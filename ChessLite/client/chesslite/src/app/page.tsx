"use client";

import { useState } from "react";
import ChessBoard from "@/components/ChessBoard";

export default function Home() {
  const [scale, setScale] = useState(1.15);
  const minScale = 1.0;
  const maxScale = 1.30;

  return (
    <main className="flex justify-center items-center min-h-screen">
      <div className="mb-4 flex items-center gap-2">
        <label className="text-white">Board Size</label>
        <input
          type="range"
          min={minScale}
          max={maxScale}
          step={0.1}
          value={scale}
          onChange={(e) => setScale(parseFloat(e.target.value))}
          className="w-40 cursor-pointer"
        />
      </div>
      <ChessBoard scale={scale}/>
    </main>
  );
}
