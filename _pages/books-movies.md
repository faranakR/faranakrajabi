---
permalink: /books-movies/
title: "Books & Movies"
layout: single
author_profile: true
classes: wide
---

<style>
.media-intro {
  max-width: 760px;
  margin: 0 auto 2.4rem;
  text-align: center;
}
.media-intro p {
  margin-bottom: .6rem;
  color: #5c6470;
  font-size: 1.05rem;
}
.media-intro .small-note {
  font-size: .82rem;
  color: #8a919b;
}
.media-section-title {
  color: #001f3f;
  margin: 2.5rem 0 1.1rem;
  padding-bottom: .55rem;
  border-bottom: 1px solid #e9edf2;
}
.movie-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 1.35rem;
  margin: 1.2rem 0 3rem;
}
.movie-card {
  display: block;
  overflow: hidden;
  border: 1px solid #e5e9ef;
  border-radius: 14px;
  background: #fff;
  text-decoration: none !important;
  color: inherit !important;
  box-shadow: 0 3px 14px rgba(0, 25, 55, .06);
  transition: transform .18s ease, box-shadow .18s ease;
}
.movie-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 9px 24px rgba(0, 25, 55, .12);
}
.poster-wrap {
  position: relative;
  aspect-ratio: 2 / 3;
  overflow: hidden;
  background: linear-gradient(145deg, #0d253f, #2b5876 55%, #4e4376);
}
.poster-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.poster-fallback {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 1rem;
  color: white;
  font-weight: 700;
  line-height: 1.2;
  z-index: 0;
}
.poster-wrap img { position: relative; z-index: 1; }
.movie-info {
  padding: .9rem .95rem 1rem;
}
.movie-title {
  margin: 0;
  color: #001f3f;
  font-size: 1rem;
  line-height: 1.25;
}
.movie-year {
  color: #8a919b;
  font-weight: 400;
}
.watch-date {
  margin: .45rem 0 0;
  color: #6c7480;
  font-size: .79rem;
  line-height: 1.3;
}
.imdb-hint {
  margin-top: .7rem;
  color: #9a7b00;
  font-size: .73rem;
  font-weight: 600;
  letter-spacing: .02em;
}
.books-placeholder {
  padding: 1.4rem;
  border: 1px dashed #ccd3dc;
  border-radius: 12px;
  color: #727a85;
  background: #fafbfc;
}
.back-personal { margin-top: 2.5rem; }
@media (max-width: 520px) {
  .movie-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .8rem; }
  .movie-info { padding: .75rem; }
  .movie-title { font-size: .9rem; }
}
</style>

<div class="media-intro">
  <p>A record of the stories I spend time with — what I read, what I watch, and eventually what I thought about them.</p>
  <p class="small-note">Movie dates are the dates I saw them in theaters. Click any movie to open its IMDb page.</p>
</div>

<h2 class="media-section-title">🎬 Movies</h2>

<div class="movie-grid">
{% assign movies = site.data.movies | sort: "sort_date" | reverse %}
{% for movie in movies %}
  <a class="movie-card" href="https://www.imdb.com/title/{{ movie.imdb_id }}/" target="_blank" rel="noopener noreferrer" aria-label="Open {{ movie.title }} on IMDb">
    <div class="poster-wrap">
      <div class="poster-fallback">{{ movie.title }}</div>
      <img
        src="https://image.thum.io/get/width/500/crop/750/noanimate/https://www.imdb.com/title/{{ movie.imdb_id }}/"
        alt="{{ movie.title }} IMDb preview"
        loading="lazy"
        onerror="this.style.display='none'">
    </div>
    <div class="movie-info">
      <h3 class="movie-title">{{ movie.title }} <span class="movie-year">({{ movie.year }})</span></h3>
      <p class="watch-date">Watched {{ movie.watched }}</p>
      <div class="imdb-hint">IMDb ↗</div>
    </div>
  </a>
{% endfor %}
</div>

<h2 class="media-section-title">📚 Books</h2>
<div class="books-placeholder">
  Book notes and reviews will live here. We can give them the same visual treatment with covers, dates read, ratings, and your reviews.
</div>

<p class="back-personal"><a href="/beyond-research/">← Back to Beyond Research</a></p>
