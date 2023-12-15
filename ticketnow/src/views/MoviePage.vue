<style scoped>
    .page {
        display: flex;
        flex-direction:  column;
    }
    .movie-bg-main {
        top: 100px;
        width: 80%;
        padding: 32px 0px;
        -moz-box-align: center;
        align-items: center;
        display: flex;
        background-repeat: no-repeat;
        background-position: right center;
        position: relative;
        margin: 0px auto;
        background-size: 100%;
        opacity: 1;
        border-radius: 10px;
    }

    .movie-bg-s1 {
        /* background-color: red; */
    }
    .movie-bg-s2 {
        min-height: fit-content;
        width: 90%;
    }
    .movie-bg-s3 {
        display: flex;
        border-radius: 16px 16px 0px 0px;
        padding: 20px 20px 20px 10px;
        background-color: rgba(56, 49, 49, 0.856);
        width: 90%;
        margin: 2px;


    }
    .poster {
        max-width: 300px;
        max-height: 500px;
        border-radius: 10px;
    }

    .poster-wrapper {
        margin-left: 20px;
    }

    .info {
        padding: 20px;
        color: rgba(255, 255, 255, 0.747) !important;
        
    }

    h1 {
        color: rgba(255, 255, 255, 0.747) !important;
    }
    p {
        text-transform: capitalize;
    }
    
    .plot {
        padding: 10px;
        color: rgba(255, 255, 255, 0.747) !important;
        background-color: black;
        width: 90%;
        margin: 2px;
    }
    .star:hover {
        cursor: pointer;
        background-color: none;
    }
    .rating {
        display: flex;
    }

    .rating-buttons button {
        border: none;
        color: none;
        margin: 0;
        margin-left: 5px;
        padding: 0;
        border-radius: 50%;
    }

    .submit {
        background-color: green;
    }
    a:hover {
        background-color:none !important;
    }
    .review {
        display: flex;
        flex-direction: column;
        justify-content: center;
        position: fixed;
        /* top: 40%; */
        left: 0;
        right: 0;
        bottom: 20px;
        margin: 0 auto !important;
        background-color: beige;
        width: 200px;
        height: 130px;
        min-width: fit-content;
        padding: 20px;
        border-radius: 20px;
        background-color: rgb(141, 118, 118)
    }
    .review div {
        margin: 2px;
    }
    
    .fieldset{
        position: relative;
        margin-bottom:20px;
        margin-top: 10px;
    }

    .fieldset input {
        border: 1px solid rgba(66, 24, 24, 0.596);
        width: 100% !important;
        padding:5px;
        height: 45px;
        font-size: 20px;
    }
    .fieldset > label {
        color: black;
        background-color: white;
        position: absolute;
        top: -12px;
        left: 20px;
        padding: 0px;
    }
    textarea {
        border-radius: 10px;
        height: 50;
        resize: none;
        padding-left: 10px;
        padding-top: 10px;
  }
  .add-review-button {
    margin-top: 10px;
    cursor: pointer;
    max-width: fit-content;
    padding: 3px;
    border-radius: 3px;
  }
  .add-review-button:active {
    background-color: antiquewhite;
    color: black;
  }

  .shows, .user-reviews {
    width: 80%;
    margin: 20px auto;
  }
    .shows {
        align-self: flex-end;
        /* margin-bottom: 150px; */
        margin-top: 100px;
        display: flex;
        flex-direction: column;
        flex-grow: 5;
    }
    .show-buttons {
        overflow-x: scroll;
        margin-top: 20px;
        display: flex;
        flex-direction: row;
        justify-content: left;
        overflow: overlay;
  }
   .show-buttons button {
    border-radius: 5px;
    color: white;
    border: none;
    padding: 10px;
    background-color:rgb(0, 128, 0);
  } 

  .show-for-date {
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    align-items: left;
    margin-bottom: 50px;
    padding: 5px;
    border-radius: 10px;
    
  }

  .anchor {
    padding: 0px;
    color: white !important;
  }

  .show-list {
    background-color: rgba(0, 0, 0, 0.747);
    padding: 10px;
    border-radius: 10px;
    margin: 10px;
    width: 100%;
  }
  
  .show-list:hover, a:hover {
    background-color: none !important;
    
  }

  .user-reviews h3 {
    margin-top: 0px;
    width: 80%;
    margin: 0 auto;
  }

    .rating-review-box {
        border-radius: 10px;
        padding: 10px;
    }

    .review-header, .review-body {
        width: 40%;
        display: flex;
        padding: 10px 20px 10px 10px;
        background-color: white;
    }

    .review-header {
        border-radius: 10px 10px 0 0;
        justify-content: space-between;
    }

    .review-body {
        border-radius: 0 0 10px 10px;
        padding-left: 40px;
    }
    h3, h2, h1 {
        color: rgba(0, 0, 0, 0.57) !important;
    }

    @media screen and (max-width: 1024px) {
        .movie-bg-main {
            width: 90%;
        }        
    }

    @media screen and (max-width: 768px) {
        .movie-bg-main, .movie-bg-s2, .movie-bg-s3 {
            width: 100%;
        }
        .rating-review-box {
            width: 100%;
        } 
        .review-header, .review-body {
            width: 90%;
            display: flex;
            padding: 10px 20px 10px 10px;
            background-color: white;
        }
        .anchor {
            width: 100%;
        }
    }

    @media screen and (max-width: 425px) {
        .movie-bg-main {
            flex-direction: column;         
        }
        .movie-bg-s3 {
            flex-direction: column;
        }
        .plot {
            width: 100%;
        }

        textarea {
            width: 95%;
        }
    }




</style>

<template>
    <div class="page">
        <div class="notification" v-if="is_unauth">
            <p>Your session has been expired. Kindly log in again.</p>
        </div>
        <div
            :style="{
                backgroundImage: 'url(' + movie.poster + ')',
            }"
            class="movie-bg-main">
            <div class="movie-bg-s1">
                <div class="movie-bg-s2">
                    <div class="movie-bg-s3">
                        <div style="border-radius: 16px 16px 0px 0px; object-fit: cover;" class="poster-wrapper">
                            <img :src="movie.poster" :alt="movie.name" class="poster"><br>
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor >= x ? 'red':'white'" role="presentation">
                                <path fill="none" d="M0 0h24v24H0V0z"></path>
                                <path fill="red" 
                                    :d="d_active">
                                </path>
                            </svg> <span style="color: white">{{ averageRating }} / 10 | {{ no_of_ratings }} rating(s)</span>
                        </div>
                    
                        <div class="info">
                            <h1><strong>{{  movie.name }}</strong></h1>
                            <hr/>
                            <p title="Language">{{  movie.language }} </p>
                            <p title="Release-date Genres Certificate">
                                {{ movie.release_date.split(" ").slice(0, 4).join(" ") }}
                                <svg data-v-8c5484d6="" xmlns="http://www.w3.org/2000/svg" width="5" height="5">
                                <circle fill="white" cx="2.5" cy="2.5" r="2.5"></circle>
                                </svg>
                                {{  movie.genres }}
                                <svg data-v-8c5484d6="" xmlns="http://www.w3.org/2000/svg" width="5" height="5">
                                <circle fill="white" cx="2.5" cy="2.5" r="2.5"></circle>
                                </svg>
                                {{ movie.certificate }}
                            </p>
                            <p title="Runtime">{{ getRuntime() }}</p>
                            <hr>
                            <p><strong>Stars</strong> {{  movie.cast }}</p><hr>
                            <p><strong>Directors</strong> {{ movie.director }}</p><hr>
                            <p><strong>Writers</strong> {{  movie.writer }}</p><hr>
                            <div class="rating">
                                <div>
                                    <svg  v-for="x in stars" :key="x" xmlns="http://www.w3.org/2000/svg" @click.prevent="rateSelect(x)" width="24" height="24" class="star" viewBox="0 0 24 24" fill="currentColor >= x ? 'red':'white'" role="presentation">
                                        <path fill="none" d="M0 0h24v24H0V0z"></path>
                                        <path :fill="currentStar >= x ? 'red':'white'" 
                                            :d="currentStar >= x? d_active : d_inactive"
                                            >
                                        </path>
                                    </svg>
                                </div>
                                <div class="rating-buttons" v-if="rate_button_show">
                                    <button @click.prevent="submitRating()" class="submit"><img src="@/assets/icons-svg/check-white.svg" alt="Submit" title="Submit"></button>
                                    <button @click.prevent="cancelRating()" class="cancel"><img src="@/assets/icons-svg/delete-white.svg" alt="Cancel" title="Cancel"></button>
                                </div>
                            </div>
                            <div v-if="currentStar > 0" class="add-review-button" @click.prevent="showReviewBox">{{  user_rating_review.review ? 'Update':'Add' }} review</div>
                        </div>
                        
                    </div>
                    <div class="plot">
                        <p>{{  movie.plot }}</p>
                    </div>
                </div>
                
            </div>
        </div>
        <div class="review" v-if="show_review_form">
            <div class="fieldset">
                <label for="review">Write your review</label>
                <textarea rows="2" cols="40" v-model="currentReview"></textarea>
            </div>
            <div class="rating-buttons">
                <button @click.prevent="submitReview()" class="submit"><img src="@/assets/icons-svg/check-white.svg" alt="Submit" title="Submit"></button>
                <button @click.prevent="cancelReview()" class="cancel"><img src="@/assets/icons-svg/delete-white.svg" alt="Cancel" title="Cancel"></button>
            </div>
        </div>
        <div class="movie-bottom">
            <div class="shows">
                <div class="show-buttons">
                    <h3 v-if="sortedShows.length == 0">No Shows Available</h3>
                    <div class="show-button" v-for="show in sortedShows" :key="show.show_id">
                        <button @click="filterShowByDate(show.start_time.split(' ').slice(0, 4).join(' '))">
                            {{  show.start_time.split(",")[0] }}<br>
                            {{  show.start_time.split(" ")[1] }}<br>
                            {{ show.start_time.split(" ")[2] }}
                        </button>
                    </div>
                </div>
                <div v-if="showSelected.length > 0">
                    <div v-for="show in showSelected" class="show-for-date">
                        <router-link class="anchor" :to="{name:'book_for_show', params: {'show_id':show.show_id}}">
                        <div class="show-list">
                            {{  show.theatre.name+", "+show.theatre.address }}<br>
                            {{ format12(show.start_time.split(" ")[4]) }}<br>
                            {{  show.theatre.screens.filter((s)=> s.screen_id == show.screen_id)[0].type_d }}
                        </div>
                        </router-link>
                    </div>
                </div>
            </div>
            <div class="user-reviews" style="{margin-top: 100px; position: relative;}">
                <h2 v-if="all_rating_reviews.length == 0">No review yet. Be the first one to review.</h2> 
                <h2 v-else>Reviews</h2>
                <div v-for="rr in all_rating_reviews" class="rating-review-box" v-if="rr?.review != null">
                    <div class="review-header"> 
                        <div>
                            <strong>{{ rr?.rating_review_id == user_rating_review?.rating_review_id ? 'You write': rr?.name+' writes' }} </strong>
                        </div>
                        <div :title="rr?.rating+'/10'">
                            <svg v-for="x in stars" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor >= x ? 'red':'white'" role="presentation">
                                <path fill="none" d="M0 0h24v24H0V0z"></path>
                                <path :fill="x <= rr?.rating ? 'red':'black'" 
                                    :d="rr?.rating >= x? d_active : d_inactive">
                                </path>
                            </svg>
                        </div>
                    </div>
                    <div class="review-body">
                        {{ rr?.review }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import { createRatingReview, getMovieById, getUser, updateRatingReviewById, getRatingReviewsByMovie, unAuthRedirect} from '@/js/requests';
import { clog, delay, convertTo12HourFormat }  from '@/js/helpers.js';
export default {
    name: "MoviePage",
    data() {
        return {
            d_inactive: "M19.65 9.04l-4.84-.42-1.89-4.45c-.34-.81-1.5-.81-1.84 0L9.19 8.63l-4.83.41c-.88.07-1.24 1.17-.57 1.75l3.67 3.18-1.1 4.72c-.2.86.73 1.54 1.49 1.08l4.15-2.5 4.15 2.51c.76.46 1.69-.22 1.49-1.08l-1.1-4.73 3.67-3.18c.67-.58.32-1.68-.56-1.75zM12 15.4l-3.76 2.27 1-4.28-3.32-2.88 4.38-.38L12 6.1l1.71 4.04 4.38.38-3.32 2.88 1 4.28L12 15.4z",
            d_active: "M12 17.27l4.15 2.51c.76.46 1.69-.22 1.49-1.08l-1.1-4.72 3.67-3.18c.67-.58.31-1.68-.57-1.75l-4.83-.41-1.89-4.46c-.34-.81-1.5-.81-1.84 0L9.19 8.63l-4.83.41c-.88.07-1.24 1.17-.57 1.75l3.67 3.18-1.1 4.72c-.2.86.73 1.54 1.49 1.08l4.15-2.5z",
            stars: [1,2,3,4,5,6,7,8,9,10],
            current_user: {
                id: null,
                first_name: "",
                last_name: "",
                email: "",
                bookings: [],
                likes: [],
                rating_reviews: [],
            },
            currentStar: 0,
            currentReview: "",
            user_rating_review: {
                rating_review_id: null,
                rating: null,
                review: "",
                user_id: null,
                movie_id: null,
            },
            movie: {
                movie_id: null,
                name: "",
                language:"",
                poster:"",
                genres: "",
                runtime_min:"",
                release_date: "",
                plot: "",
                cast: "",
                director: "",
                writer:"",
                certificate:"",
            },


            show_review_form: false,
            rating_review: {},
            showSelected: [],
            sortedShows: [],
            all_rating_reviews: [],
            is_unauth: false,
            averageRating: 0,
            no_of_ratings: 0,
        }
    },
    created() {
        this.getMovie();
        this.getCurrentUser();
        this.getAllRatingReviewByMovieId()
    },
    computed: {
        rate_button_show() {
            if (this.currentStar == 0 || this.currentStar == this.user_rating_review?.rating) {
                return false;
            }
            else if (this.currentStar > 0) {
                return true;
            }
        }
    },
    methods: {
        unAuth(e) {
            if (e.status == 401) {
                this.is_unauth = true;
                unAuthRedirect(this.$router);
                return true;
            }
            return false;
        },
        // c 
        getSortedShows(s = []) {
            return s.sort((a, b) => {
                const dateA = new Date(a.start_time.split(" -")[0]);
                const dateB = new Date(b.start_time.split(" -")[0]);
                return dateA - dateB;
         }).filter(s => {
            const currDate = new Date();
            const dateA = new Date(s.start_time.split(" -")[0]);
            return dateA >= currDate;

         });
        },
        // c
        format12(time) {
            return convertTo12HourFormat(time);
        },
        filterShowByDate(selectedDay) {
            this.showSelected =  this.movie.shows.filter(show => {
                const day = show.start_time.split(" ").slice(0, 4).join(" ");
                return day === selectedDay;
            });
        },
        //c
        async getCurrentUser() {
            try {
                const u = await getUser(this.$store.getters.getApiKey);
                this.current_user = u;
                const rating_review = this.current_user?.rating_reviews.filter(
                    (ratingReview) => ratingReview.user_id == this.current_user.id && ratingReview.movie_id==this.$route.params.id
                ) || [] ;
                if (rating_review.length > 0) {
                    this.user_rating_review = rating_review[0];
                    this.currentStar = this.user_rating_review?.rating;
                    this.currentReview = this.user_rating_review?.review
                }
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
            
        },

        async getAllRatingReviewByMovieId() {
            let id = this.$route.params.id;
            let api_key = this.$store.getters.getApiKey;
            try {
                const data = await getRatingReviewsByMovie(id, api_key);
                if (! data.error_code){
                    this.all_rating_reviews = data;
                    let count = 0;
                    let sum = 0;
                    for (const r of this.all_rating_reviews) {
                        if (r.rating > 0) {
                            count = count + 1;
                            sum = sum + r.rating;
                        } 
                    }
                    this.no_of_ratings = count
                    this.averageRating = sum / count;
                }
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        },

        getScreenFor(s_id) {
            const screen = this.movie.shows?.theatre?.screens?.filter((screen) => {
                screen.screen_id == s_id
            }) || [];
            if (screen.length > 0) {
                return screen[0];
            }
            return {}
        },

        getRuntime() {
            const hrs = Math.floor(this.movie.runtime_min/60);
            const min = this.movie.runtime_min % 60;
            let formattedRuntime = '';
            if (hrs > 0) {
                formattedRuntime += `${hrs}h `;
            }
            if (min > 0) {
                formattedRuntime += `${min}m`;
            }
            return formattedRuntime.trim();
        },    
        async getMovie() {
            let id = this.$route.params.id;
            let api_key = this.$store.getters.getApiKey;
            try {
                const data = await getMovieById(id, api_key);
                if (! data.error_code){
                    this.movie = data;
                    // delay(1000)
                    this.sortedShows = this.getSortedShows(this.movie.shows)
                    document.title = this.movie?.name
                }
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
            
        },

        async submitRating() {
            let d = {
                rating: this.currentStar,
                movie_id: this.movie.movie_id,
                user_id: this.current_user.id,
            }
            let api_key = this.$store.getters.getApiKey;

            if (this.user_rating_review.rating == undefined) {
                try {
                    
                    const rating_review = await createRatingReview(d, api_key);
                    this.currentStar = rating_review.rating;
                    this.user_rating_review = rating_review;
                } catch (e) {
                    const is_un_auth = this.unAuth(e);
                }
            }
            else if (this.currentStar != this.user_rating_review) {
                d["rating_review_id"] = this.user_rating_review.rating_review_id
                try {
                    const rating_review = await updateRatingReviewById(d, this.user_rating_review.rating_review_id, api_key);
                    this.currentStar = rating_review.rating;
                    this.user_rating_review = rating_review;
                } catch (e) {
                    const is_un_auth = this.unAuth(e);
                }    
            }
        },

        async submitReview() {
            let d = {
                rating_review_id: this.user_rating_review.rating_review_id,
                rating: this.currentStar,
                review: this.currentReview,
                movie_id: this.movie.movie_id,
                user_id: this.current_user.id,
            }
            
            let api_key = this.$store.getters.getApiKey;
            if (this.currentReview.toLocaleLowerCase() != this.user_rating_review.review.toLocaleLowerCase() && this.currentReview) {
                try {
                    const rating_review = await updateRatingReviewById(d, this.user_rating_review.rating_review_id, api_key);
                    this.currentStar = rating_review.rating;
                    this.currentReview = rating_review.review;
                    this.user_rating_review = rating_review;
                    
                } catch (e) {
                    const is_un_auth = this.unAuth(e);
                } finally {
                    this.show_review_form = false;
                }
            }
        },

        cancelRating() {
            if (this.user_rating_review.rating) {
                this.currentStar = this.user_rating_review.rating;
            }
            else {
                this.currentStar = 0;
            }
        },

        rateSelect(i) {
            this.currentStar = i;
        },

        cancelReview() {
            if (this.user_rating_review.rating_review_id) {
                this.currentReview = this.user_rating_review.review;
            }
            else {
                this.currentReview = "";
            }
            this.show_review_form = false;
        },

        showReviewBox() {
            this.show_review_form =! this.show_review_form;
        }
    }
}

</script>
