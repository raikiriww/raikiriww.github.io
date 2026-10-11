(() => {
  const data = window.__HN_SITE_DATA__ || {};
  const root = document.querySelector("[data-sidebar-root]");
  if (!root) {
    return;
  }

  function renderSection(title, items) {
    const section = document.createElement("section");
    section.className = "sidebar-section";

    const heading = document.createElement("h2");
    heading.textContent = title;
    section.appendChild(heading);

    if (!Array.isArray(items) || items.length === 0) {
      const empty = document.createElement("p");
      empty.className = "sidebar-empty";
      empty.textContent = "No entries yet.";
      section.appendChild(empty);
      return section;
    }

    const list = document.createElement("ul");
    list.className = "sidebar-list";

    for (const item of items) {
      const li = document.createElement("li");
      li.className = "sidebar-item";
      const link = document.createElement("a");
      link.href = item.href;
      link.textContent = item.label;
      li.appendChild(link);
      list.appendChild(li);
    }

    section.appendChild(list);
    return section;
  }

  root.replaceChildren(
    renderSection("Subscribe", data.subscribeLinks),
    renderSection("Recent Posts", data.recentPosts),
    renderSection("Monthly Archives", data.monthlyArchives),
    renderSection("Yearly Archives", data.yearlyArchives)
  );
})();
