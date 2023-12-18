import { GeistSans } from "geist/font/sans";
import "./globals.css";

export const metadata = {
  title: "FTB Bank AI Assistant",
  description: "FTB Bank AI Assistant - Powered by AI with DataStax",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={GeistSans.variable}>
      <body>{children}</body>
    </html>
  );
}
