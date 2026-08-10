import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Family First Legacy | Protecting What Matters Most",
  description: "Independent financial services agency helping families protect their income, prepare for retirement, and build a lasting legacy.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="scroll-smooth">
      <body>{children}</body>
    </html>
  );
}
