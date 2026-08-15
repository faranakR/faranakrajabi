---
permalink: /books-movies/
title: "Books & Movies"
layout: single
author_profile: true
classes: wide
---

<style>
.media-intro { max-width: 820px; margin: 0 0 2.5rem; }
.media-intro p { color:#5f6670; font-size:1rem; }
.media-section-title { color:#001f3f; margin:2.4rem 0 1.2rem; padding-bottom:.55rem; border-bottom:1px solid #e6e9ed; }
.movie-list { max-width: 920px; }
.movie-row { display:grid; grid-template-columns:180px minmax(0,1fr); gap:2rem; padding:1.6rem 0; border-bottom:1px solid #e8ebef; align-items:start; }
.movie-poster { width:180px; aspect-ratio:2/3; object-fit:cover; border-radius:4px; background:#eef1f4; box-shadow:0 4px 14px rgba(0,0,0,.10); display:block; }
.movie-copy h3 { margin:.05rem 0 .35rem; color:#001f3f; font-size:1.45rem; }
.movie-meta { color:#747b84; font-size:.86rem; margin-bottom:.9rem; }
.movie-rating { font-size:.92rem; font-weight:600; color:#333; margin:.15rem 0 .85rem; }
.movie-review { color:#454b53; line-height:1.7; margin:0 0 1rem; max-width:650px; }
.movie-review.empty { color:#969ca4; font-style:italic; }
.imdb-link { font-size:.84rem; font-weight:600; text-decoration:none !important; }
.books-placeholder { padding:1.3rem; border:1px dashed #ccd3dc; border-radius:8px; color:#727a85; background:#fafbfc; max-width:920px; }
@media (max-width:650px) { .movie-row { grid-template-columns:105px minmax(0,1fr); gap:1rem; padding:1.2rem 0; } .movie-poster { width:105px; } .movie-copy h3 { font-size:1.15rem; } .movie-review { font-size:.92rem; } }
</style>

<div class="media-intro">
  <p>A personal record of films I watch and books I read — when I found them, how I felt about them, and the ones that stayed with me.</p>
</div>

<h2 class="media-section-title">Movies</h2>
<div class="movie-list">
{% assign movies = site.data.movies | sort: "sort_date" | reverse %}
{% for movie in movies %}
<article class="movie-row">
  <a href="https://www.imdb.com/title/{{ movie.imdb_id }}/" target="_blank" rel="noopener noreferrer">
    <img class="movie-poster" src="{{ movie.poster }}" alt="Poster for {{ movie.title }}" loading="lazy">
  </a>
  <div class="movie-copy">
    <h3>{{ movie.title }} <span style="font-weight:400;color:#8a919b;font-size:.72em;">({{ movie.year }})</span></h3>
    <div class="movie-meta">Watched {{ movie.watched }}</div>
    <div class="movie-rating">Rating: {% if movie.rating %}{{ movie.rating }}/5{% else %}— / 5{% endif %}</div>
    {% if movie.review and movie.review != "" %}
      <p class="movie-review">{{ movie.review }}</p>
    {% else %}
      <p class="movie-review empty">Review to come.</p>
    {% endif %}
    <a class="imdb-link" href="https://www.imdb.com/title/{{ movie.imdb_id }}/" target="_blank" rel="noopener noreferrer">View on IMDb ↗</a>
  </div>
</article>
{% endfor %}
</div>

<h2 class="media-section-title">Books</h2>
<div class="books-placeholder">Book notes and reviews will live here next.</div>

<p style="margin-top:2.5rem;"><a href="/beyond-research/">← Back to Beyond Research</a></p>
