// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require("prism-react-renderer/themes/okaidia");
const darkCodeTheme = require("prism-react-renderer/themes/dracula");

const COURSE_NAME = "Complete Python Course";
const COURSE_TAGLINE = "Learn Python in 2022";
const REPO_NAME = "complete-python-course";
const COURSE_BRANDED_URL = "https://go.tecla.do/complete-python-sale";
const ALGOLIA_APP_ID = "7L8MJ964Z9";
const ALGOLIA_API_KEY = "ee562a56a85052962985c30a572b27cb";
const ALGOLIA_INDEX_NAME = "complete-python-course"; // Should match the index name in algolia.config.json

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: COURSE_NAME,
  tagline: COURSE_TAGLINE,
  url: "https://complete-python.teclado.com",
  baseUrl: "/",
  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",
  favicon: "img/favicon.ico",
  organizationName: "tecladocode",
  projectName: REPO_NAME,
  markdown: {
    mermaid: true,
  },
  themes: ["@docusaurus/theme-mermaid"],
  scripts: [
    {
      src: "https://plau-prox.teclado.workers.dev/get/script.outbound-links.js",
      defer: true,
      "data-domain": "complete-python.teclado.com",
      "data-api": "https://plau-prox.teclado.workers.dev/send/event",
    },
  ],
  presets: [
    [
      "@docusaurus/preset-classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          path: "course_contents",
          routeBasePath: "/",
          exclude: ["**/start/**", "**/end/**"],
          // Please change this to your repo.
          editUrl: `https://github.com/tecladocode/${REPO_NAME}/tree/develop/course_contents/`,
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      }),
    ],
  ],
  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      docs: {
        sidebar: {
          hideable: true,
        },
      },
      algolia: {
        // The application ID provided by Algolia
        appId: ALGOLIA_APP_ID,

        // Public API key: it is safe to commit it
        apiKey: ALGOLIA_API_KEY,

        indexName: ALGOLIA_INDEX_NAME,

        // Optional: see doc section below
        // contextualSearch: true,

        // Optional: Specify domains where the navigation should occur through window.location instead on history.push. Useful when our Algolia config crawls multiple documentation sites and we want to navigate with window.location.href to them.
        // externalUrlRegex: "external\\.com|domain\\.com",

        // Optional: Algolia search parameters
        searchParameters: {},

        // Optional: path for search page that enabled by default (`false` to disable it)
        searchPagePath: "search",
      },
      navbar: {
        title: COURSE_NAME,
        logo: {
          alt: "Teclado Logo",
          src: "img/favicon.ico",
        },
        items: [
          {
            type: "doc",
            docId: "intro/intro",
            position: "left",
            label: "Tutorial",
          },
          {
            href: COURSE_BRANDED_URL,
            label: "Get the course",
            position: "right",
          },
        ],
      },
      announcementBar: {
        id: "support_us",
        content: `<span style="font-weight: 600">Unlock all video lessons and support us by <a target="_blank" style="background-image: linear-gradient(90deg, #FF7D82, #50e3c2); background-clip: text; color: transparent; " rel="noopener noreferrer" href="${COURSE_BRANDED_URL}">buying the course</a>!</span>`,
        backgroundColor: "#1c2023",
        textColor: "#fff",
        isCloseable: false,
      },
      footer: {
        style: "dark",
        links: [
          {
            title: "Learn",
            items: [
              {
                href: COURSE_BRANDED_URL,
                label: "Get the course",
              },
              {
                label: "Tutorial",
                to: "/intro/",
              },
            ],
          },
          {
            title: "Social",
            items: [
              {
                label: "Discord",
                href: "https://go.tecla.do/discord",
              },
              {
                label: "Twitter",
                href: "https://twitter.com/jslvtr",
              },
            ],
          },
          {
            title: "More",
            items: [
              {
                label: "GitHub",
                href: `https://github.com/tecladocode/${REPO_NAME}`,
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Teclado Ltd. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
        // additionalLanguages: ["docker"],
      },
    }),
};

module.exports = config;
