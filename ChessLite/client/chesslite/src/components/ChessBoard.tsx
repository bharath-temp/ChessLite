import { useState } from "react";
import Image from "next/image";

const initialBoard = [
  ["r", "n", "b", "q", "k", "b", "n", "r"],
  ["p", "p", "p", "p", "p", "p", "p", "p"],
  ["", "", "", "", "", "", "", ""],
  ["", "", "", "", "", "", "", ""],
  ["", "", "", "", "", "", "", ""],
  ["", "", "", "", "", "", "", ""],
  ["P", "P", "P", "P", "P", "P", "P", "P"],
  ["R", "N", "B", "Q", "K", "B", "N", "R"],
];

const pieceMap: { [key: string]: string } = {
  r: "/assets/chess/black_rook.svg",
  n: "/assets/chess/black_knight.svg",
  b: "/assets/chess/black_bishop.svg",
  q: "/assets/chess/black_queen.svg",
  k: "/assets/chess/black_king.svg",
  p: "/assets/chess/black_pawn.svg",
  R: "/assets/chess/white_rook.svg",
  N: "/assets/chess/white_knight.svg",
  B: "/assets/chess/white_bishop.svg",
  Q: "/assets/chess/white_queen.svg",
  K: "/assets/chess/white_king.svg",
  P: "/assets/chess/white_pawn.svg",
};

interface ChessBoardProps {
  scale: number;
}

export default function ChessBoard({ scale }: ChessBoardProps) {
  const squareSize = `${4 * scale}rem`; // Dynamic square size
  const pieceSize = 55 * scale; // Scale piece size in pixels

  return (
    <div className="flex flex-col items-center">
      {/* Chessboard */}
      <div className="grid grid-cols-8 border-4 border-gray-800">
        {initialBoard.flat().map((piece, index) => {
          const row = Math.floor(index / 8);
          const col = index % 8;
          const isDark = (row + col) % 2 === 1;

          return (
            <div
              key={index}
              className="flex items-center justify-center"
              style={{
                width: squareSize,
                height: squareSize,
                backgroundColor: isDark ? "#6b7280" : "#d1d5db",
              }}
            >
              {piece && (
                <Image
                  src={pieceMap[piece]}
                  alt={piece}
                  width={pieceSize}
                  height={pieceSize}
                  className="object-contain"
                />
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
