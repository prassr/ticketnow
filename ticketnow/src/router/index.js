import {createRouter, createWebHistory} from 'vue-router';
import LandingPage from '../views/LandingPage.vue';
import LoginPage from '../views/LoginPage.vue';
import LoginForm from '../components/LoginForm.vue';
import SignupForm from '../components/SignupForm.vue';
import ResetPassword from '../components/ResetPassword.vue';
import AdminPage from "../views/AdminPage.vue";
import AdminMoviePage from "../views/AdminMoviePage.vue";
import AdminTheatrePage from "../views/AdminTheatrePage.vue";
import AdminShowPage from "../views/AdminShowPage.vue";
import AdminReportPage from "../views/AdminReportPage.vue";
import AdminTheatreScreenPage from "../views/AdminTheatreScreenPage.vue";
import UserPage from "../views/UserPage.vue";
import UserMoviePage from "../views/UserMoviePage.vue";
import ShowPage from "../views/ShowPage.vue";
import TheatrePage from "../views/TheatrePage.vue";
import UserBookingPage from "../views/UserBookingPage.vue";
import MoviePage from "../views/MoviePage.vue";

const routes = [
  {
    path: "/",
    name: "langing",
    redirect: "/in",
  },
  {
    path: "/in",
    component: LandingPage,
    name: 'landing',
    children: [
      {
        path: "login",
        name: "login",
        component: LoginForm,
        props: true,
      },
      {
        path: "signup",
        name: "signup",
        component: SignupForm
      },
      {
        path: "password_reset",
        name: "password_reset",
        component: ResetPassword,
        props: true,
      },
    ]
  },
  {
    path:"/in/u",
    name:"user_home",
    component: UserPage,//UserProfile,
    redirect: "/in/u/movies",
    children: [
        {
            path: "profile",
            name: "user_profile",
            component: "",
        },
      {
        path: "movies",
        name: "user_movies",
        component: UserMoviePage,
      },
        {
            path: "movie/:id",
            name: "explore_movie",
            component: MoviePage,
            props: true,

        },
      {
        path: "shows",
        name: "user_shows",
        component: "", // Shows.vue
        children: [
          {
            path:":show_id",
            props: true,
            name: "book_for_show",
            component: ShowPage // add component here.
          },
        ]
      },
            {
                path: "theatres",
                name: "explore_venue",
                component: TheatrePage,
            },
      {
        path: "bookings",
        name: "user_bookings",
        component: UserBookingPage,
      },
    ]
  },
    {
        path: "/in/a",
        name: "admin_home",
        redirect: "/in/a/movies",
        component: AdminPage,
        children: [
            {
                path: "theatres",
                name: "theatre_handler",
                component: AdminTheatrePage, // Admin theatre to add theatre
            },

            {
                path: "theatre/:theatreId",
                name: "theatre_screen_handler",
                props: true,
                component: AdminTheatreScreenPage
            },
            {
                path: "movies",
                name: "movie_handler",
                component: AdminMoviePage, // Admin movies to add movies
            },
            {
                path: "shows",
                name: "show_handler",
                component: AdminShowPage, // to create new show
            },
            {
                path: "report",
                name: "report_handler",
                component: AdminReportPage // for getting bookings data
            },
        ]
    }
  ]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
