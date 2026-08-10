"use client";

import React from "react";

export default function NumbersBand() {
  return (
    <section id="numbers">
      <div className="container-full">
        <div className="numbers-grid">
          <div className="number-item">
            <div className="ni-num">EDUCATION FIRST</div>
            <div className="ni-label">Clear explanations before decisions</div>
          </div>
          <div className="number-item">
            <div className="ni-num">1-ON-1 GUIDANCE</div>
            <div className="ni-label">Personal support that starts with listening</div>
          </div>
          <div className="number-item">
            <div className="ni-num">FAMILY FOCUSED</div>
            <div className="ni-label">Planning around the people you love</div>
          </div>
          <div className="number-item">
            <div className="ni-num">LICENSED GUIDANCE</div>
            <div className="ni-label">Professionals who explain before recommending</div>
          </div>
        </div>
      </div>
    </section>
  );
}
