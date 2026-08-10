import { defineConfig } from "tinacms";

// TinaCMS configuration for 100% open-source visual editing
const branch = process.env.GITHUB_BRANCH || process.env.VERCEL_GIT_COMMIT_REF || "main";

export default defineConfig({
  branch,

  // Get this from tina.io if using Tina Cloud, or leave blank for local/git-backed mode
  clientId: process.env.NEXT_PUBLIC_TINA_CLIENT_ID || "",
  token: process.env.TINA_TOKEN || "",

  build: {
    outputFolder: "admin",
    publicFolder: "public",
  },
  media: {
    tina: {
      mediaRoot: "images",
      publicFolder: "public",
    },
  },
  // Schema definitions for visual editing
  schema: {
    collections: [
      {
        name: "page",
        label: "Pages",
        path: "content/pages",
        format: "md",
        fields: [
          {
            type: "string",
            name: "title",
            label: "Page Title",
            isTitle: true,
            required: true,
          },
          {
            type: "string",
            name: "description",
            label: "Meta Description",
            ui: {
              component: "textarea",
            },
          },
          {
            type: "string",
            name: "language",
            label: "Language",
            options: ["en", "es"],
          },
          {
            type: "rich-text",
            name: "body",
            label: "Body Content",
            isBody: true,
          },
        ],
      },
      {
        name: "heroSlide",
        label: "Hero Slides",
        path: "content/hero-slides",
        format: "json",
        fields: [
          {
            type: "string",
            name: "title",
            label: "Slide Title",
            isTitle: true,
            required: true,
          },
          {
            type: "string",
            name: "eyebrow",
            label: "Eyebrow Text",
          },
          {
            type: "string",
            name: "subtitle",
            label: "Subtitle / Description",
            ui: {
              component: "textarea",
            },
          },
          {
            type: "string",
            name: "ctaPrimaryText",
            label: "Primary Button Text",
          },
          {
            type: "string",
            name: "ctaPrimaryLink",
            label: "Primary Button Link",
          },
          {
            type: "string",
            name: "ctaSecondaryText",
            label: "Secondary Button Text",
          },
          {
            type: "string",
            name: "ctaSecondaryLink",
            label: "Secondary Button Link",
          },
          {
            type: "image",
            name: "bgImage",
            label: "Background Image",
          },
          {
            type: "string",
            name: "language",
            label: "Language",
            options: ["en", "es"],
          },
        ],
      },
      {
        name: "faq",
        label: "FAQs",
        path: "content/faqs",
        format: "json",
        fields: [
          {
            type: "string",
            name: "question",
            label: "Question",
            isTitle: true,
            required: true,
          },
          {
            type: "string",
            name: "answer",
            label: "Answer",
            ui: {
              component: "textarea",
            },
            required: true,
          },
          {
            type: "string",
            name: "category",
            label: "Category",
            options: ["general", "services", "business", "opportunity"],
          },
          {
            type: "string",
            name: "language",
            label: "Language",
            options: ["en", "es"],
          },
        ],
      },
    ],
  },
});
