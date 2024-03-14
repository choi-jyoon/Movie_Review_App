import React from 'react';
import axios from 'axios';
import Movie from '../pages/Movie';
import './Home.css';

class Home extends React.Component{
    state = {
        isLoading: true,
        movies: [],
      };
    
      getMovies = async () => {
        const { data: {movies} } = await axios.get('/movies');
      
        console.log(movies);
        this.setState({movies, isLoading:false});
      };
    
      componentDidMount() {
        this.getMovies(); // 컴포넌트가 마운트되면 영화 데이터 가져오기
      }
    
      render() {
        const {isLoading, movies} = this.state;
        return (
          <section className="container">
            {isLoading? (
              <div className="loader">
                <span className="loader_text">loading...</span>
              </div>
            ):
            (
              <div className="movies">
                {
                  movies.map(movie => (
                    <Movie 
                    key = {movie.id}
                    id = {movie.id}
                    title = {movie.title}
                    percent = {movie.percent}
                    release = {movie.release}
                    image = {movie.img}
                    />
                  ))
                }
              </div>
            )} 
          </section>
        );
      }
}
export default Home;