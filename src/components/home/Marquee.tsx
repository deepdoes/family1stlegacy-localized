"use client";

import React from "react";

export default function Marquee() {
  const items = [
    "Life Insurance",
    "Retirement Planning",
    "Education Savings",
    "Estate Preservation",
    "Wealth Building",
    "Business Strategies",
    "Career Opportunity",
  ];

  return (
    <div id="marquee" aria-hidden="true">
      <div className="marquee-track">
        {/* Repeat twice for seamless infinite marquee loop */}
        {[...items, ...items].map((item, idx) => (
          <span key={idx} className="marquee-item">
            {item} <span>—</span>
          </span>
        ))}
      </div>
    </div>
  );
}
