import axios from "axios";
import * as fs from "fs";
import * as path from "path";
import sharp from "sharp";
import { fileURLToPath } from "url";

const BASE_URL = "https://upload.wikimedia.org/wikipedia/commons"
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const TARGET_DIR = path.resolve(__dirname, "../src/public/assets/chess");

const CHESS_PIECE_MAP = {
    white: {
        king: "4/42/Chess_klt45.svg",
        flipped_king: "1/17/Chess_flt45.svg",
        queen: "1/15/Chess_qlt45.svg",
        flipped_queen: "f/f0/Chess_glt45.svg",
        rook: "7/72/Chess_rlt45.svg",
        flipped_rook: "d/d0/Chess_mlt45.svg",
        bishop: "b/b1/Chess_blt45.svg",
        flipped_bishop: "7/7c/Chess_Blt45.svg",
        knight: "7/70/Chess_nlt45.svg",
        flipped_knight: "1/17/Chess_Nlt45.svg",
        pawn: "4/45/Chess_plt45.svg",
        flipped_pawn: "0/08/Chess_hlt45.svg",
    },
    black: {
        king: "f/f0/Chess_kdt45.svg",
        flipped_king: "2/2c/Chess_fdt45.svg",
        queen: "4/47/Chess_qdt45.svg",
        flipped_queen: "3/31/Chess_gdt45.svg",
        rook: "f/ff/Chess_rdt45.svg",
        flipped_rook: "c/cd/Chess_mdt45.svg",
        bishop: "9/98/Chess_bdt45.svg",
        flipped_bishop: "5/5a/Chess_Bdt45.svg",
        knight: "e/ef/Chess_ndt45.svg",
        flipped_knight: "4/43/Chess_Ndt45.svg",
        pawn: "c/c7/Chess_pdt45.svg",
        flipped_pawn: "d/dd/Chess_hdt45.svg",
    },
};

async function downloadImage(fileName: string, targetPath: string): Promise<void> {
    const url = `${BASE_URL}/${fileName}`;
    try {
        console.log(`Downloading: ${url}`)
        const resp = await axios.get(url, { responseType: "arraybuffer" });
        fs.writeFileSync(targetPath, resp.data)
        console.log(`Saved: ${targetPath}`)
    } catch (error) {
        if (error instanceof Error) {
            console.error(`Failed to download ${url}: ${error.message}`);
        } else {
            console.error(`Failed to download ${url}: ${error}`);
        }
    }
}

async function downloadAndGenerateAssets(): Promise<void> {
    for (const [color, pieces] of Object.entries(CHESS_PIECE_MAP)) {
        for (const [type, fileName] of Object.entries(pieces)) {
            const targetPath = path.join(TARGET_DIR, `${color}_${type}.svg`);
            await downloadImage(fileName, targetPath);
        }
    }
}

downloadAndGenerateAssets()
  .then(() => console.log("All chess assets downloaded and rotated successfully!"))
  .catch((error) => console.error(`Error processing chess assets: ${error.message}`));