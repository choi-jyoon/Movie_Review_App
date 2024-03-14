import React from 'react';
import { Link } from 'react-router-dom';
import './Navigation.css';

function Navigation() {
  return (
    <div className="nav">
      <Link to="/">실시간 상영 영화</Link>
      <Link to="/review">영화 리뷰 보기</Link>
    </div>
  );
}

export default Navigation;