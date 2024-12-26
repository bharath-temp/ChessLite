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
        queen: "1/15/Chess_qlt45.svg",
        rook: "7/72/Chess_rlt45.svg",
        bishop: "b/b1/Chess_blt45.svg",
        knight: "7/70/Chess_nlt45.svg",
        pawn: "4/45/Chess_plt45.svg",
    },
    black: {
        king: "f/f0/Chess_kdt45.svg",
        queen: "4/47/Chess_qdt45.svg",
        rook: "f/ff/Chess_rdt45.svg",
        bishop: "9/98/Chess_bdt45.svg",
        knight: "e/ef/Chess_ndt45.svg",
        pawn: "c/c7/Chess_pdt45.svg",
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

async function rotateAsset(originalPath: string, rotatedPath: string): Promise<void> {
    try {
        console.log(`Rotating: ${originalPath}`);
        const buffer = fs.readFileSync(originalPath);
        const rotatedBuffer = await sharp(buffer).rotate(180).toBuffer();
        fs.writeFileSync(rotatedPath, rotatedBuffer);
        console.log(`Saved rotated: ${rotatedPath}`);
    } catch (error) {
        if (error instanceof Error) {
            console.error(`Failed to rotate ${originalPath}: ${error.message}`);
        } else {
            console.error(`Failed to rotate ${originalPath}: ${error}`);
        }
    }
}

async function downloadAndGenerateAssets(): Promise<void> {
    for (const [color, pieces] of Object.entries(CHESS_PIECE_MAP)) {
        for (const [type, fileName] of Object.entries(pieces)) {
            const targetPath = path.join(TARGET_DIR, `${color}_${type}.svg`);
            const rotatedPath = path.join(TARGET_DIR, `${color}_${type}_flipped.svg`);
            
            await downloadImage(fileName, targetPath);
            await rotateAsset(targetPath, rotatedPath);
        }
    }
}

downloadAndGenerateAssets()
  .then(() => console.log("All chess assets downloaded and rotated successfully!"))
  .catch((error) => console.error(`Error processing chess assets: ${error.message}`));