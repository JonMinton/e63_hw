const baseURL = 'http://localhost:9000/api/sightings/'

export const getSightings = () => {
    return fetch(baseURL)
        .then(res => res.json())
}

export const postSighting = (payload) => {
    return fetch(baseURL, {
        method: 'POST',
        body: JSON.stringify(payload),
        headers: { 'Content-Type': 'application/json' }
    })
    .then(res => res.json())
    .then(data => {
      return {
        ...data,
        ...payload
      }
    })
}

export const deleteSighting = (id) => {
    return fetch(baseURL + id, {
        method: 'DELETE'
    })
}

export const updateSighting = (id, payload) => {
    return fetch(baseURL + id, {
        method: 'PUT',
        body: JSON.stringify(payload),
        headers: { 'Content-Type': 'application/json'}
    })
    .then(res => res.json())
    .then(data => {
      return {
        ...data, // { _id: <> }
        ...payload // { name: <> }
      }
    })
}

