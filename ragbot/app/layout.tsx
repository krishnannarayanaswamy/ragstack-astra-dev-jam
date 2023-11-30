import { GeistSans } from "geist/font/sans";
import "./globals.css";

export const metadata = {
  title: "FTB ChatBot",
  description: "FTB ChatBot - Powered by AI with DataStax",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={GeistSans.variable}>
      <body>{children}</body>
    </html>
  );
}
