import  {base_url} from './api_config.js'


export function unAuthRedirect(router) {  
    setTimeout(()=> {
        router.push({name:"landing"})
    }, 10*1000)
}


export async function sendSignupOTP(body) {
  try {
    const response = await fetch(base_url+"/signup/otp", {
      headers : {
        "Content-Type":'application/json'
      },
      method: "POST",
      body : JSON.stringify(body)
    })
 
    const data = await response.json();
    
    if (response.ok) {
      return data;
    }
    else {
      throw response;
    }
  }
  catch(e) {
    throw e
  }
}

export async function verifyOTP(body) {
  try {
    const response = await fetch(base_url+"/verify-otp", {
      headers : {
        "Content-Type":'application/json'
      },
      method: "POST",
      body : JSON.stringify(body)
    })
 
    const data = await response.json();
    if (response.ok) {
      return data;
    }
    else {
      throw response;
    }
  }
  catch(e) {
    throw e;
  }
}

export async function createUser(body) {
  try {
    const response = await fetch(base_url+"/user", {
      headers : {
        "Content-Type":'application/json'
      },
      method: "POST",
      body : JSON.stringify(body)
    })
 
    const data = await response.json();
    if (response.ok) {
            console.log(data)
      return data;
    }
    else {
      throw data
    }
  }
  catch(e) {
    console.log(e)
  }
}

export async function appLogin(body, query) {
    try {
        const response = await fetch(base_url+"/login?"+new URLSearchParams(query), {
            headers : {
                "Content-Type":'application/json',
            },
            method: "POST",
            mode:"cors",
            credentials: 'same-origin',
            body : JSON.stringify(body)
        })
        const data = await response.json();
        if (response.ok) {
            return data;
        }
        else {
            throw data;
        }
    }
    catch(e) {
        throw e;
    }
}

export async function signOut(store, cookies, router) {
    try {
        const response = await fetch(base_url+"/logout", {
            headers : {
                "Content-Type":'application/json',
                "Authorization": `Bearer ${store.getters.getApiKey}`,
            },
            method: "GET",
        })
        const data = await response.json();
        if (response.ok) {
            return true;
        }

    } catch (e) {
        alert("Something went wrong. Kindly log in again.");
    }
    finally {
        cookies.remove("x-access-token");
        store.commit("setApiKey", null);
        router.push("/in");
    }
}

export async function sendPasswordResetOTP(body) {
  try {
    const response = await fetch(base_url+"/password-reset-otp", {
      headers : {
        "Content-Type":'application/json'
      },
      method: "POST",
      body : JSON.stringify(body)
    })
 
    const data = await response.json();
    if (response.ok) {
      return data;
    }
    else {
      throw data
    }
  }
  catch(e) {
    throw e
  }
}

export async function passwordReset(body) {
  try {
    const response = await fetch(base_url+"/password-reset", {
      headers : {
        "Content-Type":'application/json'
      },
      method: "POST",
      body : JSON.stringify(body)
    })
 
    const data = await response.json();
    if (response.ok) {
      return data;
    }
    else {
      throw data
    }
  }
  catch(e) {
    throw e
  }
}


// USER

export async function getUser(key) {
    console.log(key);
    try {
        const response = await fetch(base_url+"/user/u", {
            headers: {
                "Content-Type":'application/json',
                "Authorization": `Bearer ${key}`,
            },
            method: "GET",
        })
        const data = await response.json();
        if (!response.ok) {
            throw response
        }
        if (response.ok) {
            return data;
        }
    } catch(e) {
        throw e;
    }

}


// MOVIE

export async function createMovie(body, key) {
    try {
        const response = await fetch(base_url+"/movie", {
            headers: {
                "Content-Type":'application/json',
                "Authorization": `Bearer ${key}`,
            },
            method: "POST",
            body: JSON.stringify(body),
        })
        const data = await response.json();
        if (!response.ok) {
            throw response
        }
        if (response.ok) {
            return data;
        }
    } catch(e) {
        throw e;
    }
}


export async function getMovies(key) {
    try {
        const response = await fetch(base_url+"/movie", {
            headers: {
                "Content-Type":'application/json',
                "Authorization": `Bearer ${key}`,
            },
            method: "GET",
        })
        const data = await response.json();
        if (!response.ok) {
            throw response
        }
        if (response.ok) {
            return data;
        }
    } catch(e) {
        throw e;
    }

}

export async function getMoviesForShow(key) {
    try {
        const response = await fetch(base_url+"/movie_show", {
            headers: {
                "Content-Type":'application/json',
                "Authorization": `Bearer ${key}`,
            },
            method: "GET",
        })
        const data = await response.json();
        if (!response.ok) {
            throw response
        }
        if (response.ok) {
            if (response.error_code) {
                throw data;
            }
            return data;
        }
    } catch(e) {
        throw e;
    }
}


export async function updateMovieById(body, id, key) {
try {
    const response = await fetch(base_url+"/movie/"+id, {
        headers: {
            "Content-Type":'application/json',
            "Authorization": `Bearer ${key}`,
        },
        method: "PUT",
        body: JSON.stringify(body),

    })
    const data = await response.json();
   
    if (!response.ok) {
        throw response
    }
    
    if (response.ok) {
        return data;
    }
} catch(e) {
    throw e;
}

}

export async function deleteMovieById(id, key) {
  try {
      const response = await fetch(base_url+"/movie/"+id, {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "DELETE",

      })
      const data = await response.json();
    if (!response.ok) {
        throw response
    }
    if (response.ok) {
        return data;
    }
  } catch(e) {
      throw e;
  }

}

export async function getMovieById(id, key) {
    console.log(key);
    try {
        const response = await fetch(base_url+"/movie/"+id, {
            headers: {
                "Content-Type":'application/json',
                "Authorization": `Bearer ${key}`,
            },
            method: "GET",
        })
        
        const data = await response.json();
        if (! response.ok) {
            throw response;
        }
        if (response.ok) {
            return data;
        }
    } catch(e) {
        throw e;
    }

}

export async function createTheatre(body, key) {
  try {
      const response = await fetch(base_url+"/theatre", {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "POST",
          body: JSON.stringify(body),
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
        }
      if (response.ok) {
          return data;
      }
  } catch(e) {
      throw e;
  }
}


export async function getTheatres(key) {
  try {
      const response = await fetch(base_url+"/theatre", {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          mode: "cors",
          method: "GET",
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
    }
      if (response.ok) {
          return data;
      }
  } catch(e) {
      throw e;
  }

}

export async function updateTheatreById(body, id, key) {
try {
    const response = await fetch(base_url+"/theatre/"+id, {
        headers: {
            "Content-Type":'application/json',
            "Authorization": `Bearer ${key}`,
        },
        method: "PUT",
        body: JSON.stringify(body),

    })
    const data = await response.json();
    if (!response.ok) {
        throw response
    }
    if (response.ok) {
        return data;
    }
} catch(e) {
    throw e;
}

}

export async function deleteTheatreById(id, key) {
try {
    const response = await fetch(base_url+"/theatre/"+id, {
        headers: {
            "Content-Type":'application/json',
            "Authorization": `Bearer ${key}`,
        },
        method: "DELETE",

    })
    const data = await response.json();
    if (!response.ok) {
        throw response
    }
    if (response.ok) {
        return data;
    }
} catch(e) {
    throw e;
}

}

export async function getTheatreById(id, key) {
  try {
      const response = await fetch(base_url+"/theatre/"+id, {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "GET",
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
    }
      if (response.ok) {
          return data;
      }
  } catch(e) {
      throw e;
  }
}

export async function createShow(body, key) {
  try {
      const response = await fetch(base_url+"/show", {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "POST",
          body: JSON.stringify(body),
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
    }
      if (response.ok) {
          return data;
      }
  } catch(e) {
      throw e;
  }
}


export async function getShows(key) {
  try {
      const response = await fetch(base_url+"/show", {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "GET",
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
    }
      if (response.ok) {
          return data;
      }
  } catch(e) {
      throw e;
  }

}

export async function getShowsByTheatre(key) {
  try {
      const response = await fetch(base_url+"/theatre/shows", {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "GET",
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
    }
      if (response.ok) {
          return data;
      }
  } catch(e) {
      throw e;
  }

}


export async function getRatingReviewsByMovie(id, key) {
    try {
        const response = await fetch(base_url+"/movie/"+id+"/rating_reviews", {
            headers: {
                "Content-Type":'application/json',
                "Authorization": `Bearer ${key}`,
            },
            method: "GET",
        })
        const data = await response.json();
        if (! response.ok) {
            throw response;
        }
        if (response.ok) {
            return data;
        }
    } catch(e) {
        throw e;
    }
  
  }


export async function updateShowById(body, id, key) {
try {
    const response = await fetch(base_url+"/show/"+id, {
        headers: {
            "Content-Type":'application/json',
            "Authorization": `Bearer ${key}`,
        },
        method: "PUT",
        body: JSON.stringify(body),

    })
    const data = await response.json();
    if (!response.ok) {
        throw response
    }
    if (response.ok) {
        return data;
    }
} catch(e) {
    throw e;
}

}

export async function deleteShowById(id, key) {
try {
    const response = await fetch(base_url+"/show/"+id, {
        headers: {
            "Content-Type":'application/json',
            "Authorization": `Bearer ${key}`,
        },
        method: "DELETE",

    })
    const data = await response.json();
    if (!response.ok) {
        throw response
    }
    if (response.ok) {
        return data;
    }
} catch(e) {
    throw e;
}

}

export async function getShowById(id, key) {
  try {
      const response = await fetch(base_url+"/show/"+id, {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "GET",
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
    }
      if (response.ok) {
          return data;
      }
  } catch(e) {
      throw e;
  }
}

export async function createBooking(body, key) {
  try {
      const response = await fetch(base_url+"/booking", {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "POST",
          body: JSON.stringify(body),
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
    }
      if (response.ok) {
          return data;
      }
  } catch(e) {
      throw e;
  }
}


export async function getBookings(key) {
  try {
      const response = await fetch(base_url+"/booking", {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "GET",
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
    }
      if (response.ok) {
          return data;
      }
  } catch(e) {
      throw e;
  }

}

export async function updateBookingById(body, id, key) {
try {
    const response = await fetch(base_url+"/booking/"+id, {
        headers: {
            "Content-Type":'application/json',
            "Authorization": `Bearer ${key}`,
        },
        method: "PUT",
        body: JSON.stringify(body),

    })
    const data = await response.json();
    if (!response.ok) {
        throw response
    }
    if (response.ok) {
        return data;
    }
} catch(e) {
    throw e;
}

}

export async function deleteBookingById(id, key) {
try {
    const response = await fetch(base_url+"/booking/"+id, {
        headers: {
            "Content-Type":'application/json',
            "Authorization": `Bearer ${key}`,
        },
        method: "DELETE",

    })
    const data = await response.json();
    if (!response.ok) {
        throw response
    }
    if (response.ok) {
        return data;
    }
} catch(e) {
    throw e;
}

}

export async function getBookingsByShowId(id, key) {
  try {
      const response = await fetch(base_url+"/booking/show/"+id, {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "GET",
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
    }
      if (response.ok) {
          return data;
      }
  } catch(e) {
      throw e;
  }
}

export async function getBookingsByUser(key) {
  try {
      const response = await fetch(base_url+"/user/bookings", {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "GET",
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
    }
      if (response.ok) {
        console.log(data)
          return data;
      }
  } catch(e) {
      throw e;
  }
}


export async function getAvailableSeatsByShowId(id, key) {
  try {
      const response = await fetch(base_url+"/booking/show/"+id+"/seats_available", {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "GET",
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
    }
      if (response.ok) {
          return data;
      }
  } catch(e) {
      throw e;
  }
}


export async function createScreen(body, key) {
  try {
      const response = await fetch(base_url+"/screen", {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "POST",
          body: JSON.stringify(body),
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
    }
      if (response.ok) {
          return data;
      }
  } catch(e) {
      throw e;
  }
}


export async function getScreens(key) {
  try {
      const response = await fetch(base_url+"/screen", {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "GET",
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
    }
      if (response.ok) {
          return data;
      }
  } catch(e) {
      throw e;
  }

}

export async function updateScreenById(body, id, key) {
try {
    const response = await fetch(base_url+"/screen/"+id, {
        headers: {
            "Content-Type":'application/json',
            "Authorization": `Bearer ${key}`,
        },
        method: "PUT",
        body: JSON.stringify(body),

    })
    const data = await response.json();
    if (!response.ok) {
        throw response
    }
    if (response.ok) {
        return data;
    }
} catch(e) {
    throw e;
}

}

export async function deleteScreenById(id, key) {
try {
    const response = await fetch(base_url+"/screen/"+id, {
        headers: {
            "Content-Type":'application/json',
            "Authorization": `Bearer ${key}`,
        },
        method: "DELETE",

    })
    const data = await response.json();
    if (!response.ok) {
        throw response
    }
    if (response.ok) {
        return data;
    }
} catch(e) {
    throw e;
}

}

export async function getScreenById(id, key) {
  try {
      const response = await fetch(base_url+"/screen/"+id, {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "GET",
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
    }
      if (response.ok) {
          return data;
      }
  } catch(e) {
      throw e;
  }
}

export async function createLike(body, key) {
  try {
      const response = await fetch(base_url+"/like", {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "POST",
          body: JSON.stringify(body),
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
    }
      if (response.ok) {
          return data;
      }
  } catch(e) {
      throw e;
  }
}


export async function getLikes(key) {
  try {
      const response = await fetch(base_url+"/like", {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "GET",
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
    }
      if (response.ok) {
          return data;
      }
  } catch(e) {
      throw e;
  }

}

export async function updateLikeById(body, id, key) {
try {
    const response = await fetch(base_url+"/like/"+id, {
        headers: {
            "Content-Type":'application/json',
            "Authorization": `Bearer ${key}`,
        },
        method: "PUT",
        body: JSON.stringify(body),

    })
    const data = await response.json();
    if (!response.ok) {
        throw response
    }
    if (response.ok) {
        return data;
    }
} catch(e) {
    throw e;
}

}

export async function deleteLikeById(id, key) {
try {
    const response = await fetch(base_url+"/like/"+id, {
        headers: {
            "Content-Type":'application/json',
            "Authorization": `Bearer ${key}`,
        },
        method: "DELETE",

    })
    const data = await response.json();
    if (!response.ok) {
        throw response
    }
    if (response.ok) {
        return data;
    }
} catch(e) {
    throw e;
}

}

export async function getLikeById(id, key) {
  try {
      const response = await fetch(base_url+"/like/"+id, {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "GET",
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
    }
      if (response.ok) {
          return data;
      }
  } catch(e) {
      throw e;
  }
}

export async function createRatingReview(body, key) {
  try {
      const response = await fetch(base_url+"/rating-review", {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "POST",
          body: JSON.stringify(body),
      })
      const data = await response.json();
      if (!response.ok) {
        return data;
    }   
      if (response.ok) {
          return data;
      }
  } catch(e) {
      throw e;
  }
}


export async function getRatingReviews(key) {
  try {
      const response = await fetch(base_url+"/rating-review", {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "GET",
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
    }
      if (response.ok) {
          return data;
      }
  } catch(e) {
      throw e;
  }

}

export async function updateRatingReviewById(body, id, key) {
try {
    const response = await fetch(base_url+"/rating-review/"+id, {
        headers: {
            "Content-Type":'application/json',
            "Authorization": `Bearer ${key}`,
        },
        method: "PUT",
        body: JSON.stringify(body),

    })
    const data = await response.json();
    if (!response.ok) {
        throw response
    }
    if (response.ok) {
        return data;
    }
} catch(e) {
    throw e;
}

}

export async function deleteRatingReviewById(id, key) {
try {
    const response = await fetch(base_url+"/rating-review/"+id, {
        headers: {
            "Content-Type":'application/json',
            "Authorization": `Bearer ${key}`,
        },
        method: "DELETE",

    })
    const data = await response.json();
    if (!response.ok) {
        throw response
    }
    if (response.ok) {
        return data;
    }
} catch(e) {
    throw e;
}

}

export async function getRatingReviewById(id, key) {
  try {
      const response = await fetch(base_url+"/rating-review/"+id, {
          headers: {
              "Content-Type":'application/json',
              "Authorization": `Bearer ${key}`,
          },
          method: "GET",
      })
      const data = await response.json();
      if (!response.ok) {
        throw response
    }
        return data;
  } catch(e) {
      throw e;
  }
}


export async function generateReport(query, key) {
    try {
        const queryParams = new URLSearchParams(query).toString();
        const url = base_url+"/admin/generate-report?"+queryParams
        console.log(url);
        const response = await fetch(url, {
            headers: {
                "Content-Type":'application/json',
                "Authorization": `Bearer ${key}`,
            },
            method: "GET",
            
        })
        const data = await response.json();
        if (!response.ok) {
          throw response
      }
      return data;
    } catch(e) {
        throw e;
    }
  }
  
  