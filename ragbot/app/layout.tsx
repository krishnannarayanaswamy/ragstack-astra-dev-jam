import { GeistSans } from "geist/font/sans";
import "./globals.css";

export const metadata = {
  title: "SBI LY HOUR ChatBot",
  description: "SBI LY HOUR ChatBot - Powered by AI with DataStax",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={GeistSans.variable}>
      <body>{children}</body>
    </html>
  );
}
