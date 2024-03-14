import React from "react";
import PropTypes from'prop-types';
import './Movie.css'

// Movie 컴포넌트 정의
function Movie({ id, title, release, percent, image }) {
    return (
      <div className="movie">
        <img src={image} alt={title} title={title}/>
        <div className="movie_data">
          <h2 className="movie_title">{title}</h2>
          <p className="movie_percent">예매율: {percent}</p>
          <p className="movie_release">개봉일: {release}</p>
        </div>
      </div>
    );
  }


// Movie 컴포넌트의 props 타입 검사
Movie.propTypes = {
    id: PropTypes.number.isRequired,
    title: PropTypes.string.isRequired,
    release: PropTypes.string.isRequired,
    percent: PropTypes.string.isRequired,
    image: PropTypes.string.isRequired,
  };

export default Movie;