import { useState, useEffect, Dispatch, SetStateAction } from "react";
import axios from "axios";

interface AxiosState<T> {
  readonly data: T | null;
  readonly error: {
    status: number;
    statusText: string;
    data: { detail: string };
  } | null;
  readonly loading: boolean;
}

type AxiosCallback<T> = (
  state: AxiosState<T>,
  setState: Dispatch<SetStateAction<AxiosState<T>>>
) => void;

function useAxios<T>(callback: AxiosCallback<T>): AxiosState<T> {
  const [state, setState] = useState<AxiosState<T>>({
    data: null,
    error: null,
    loading: true,
  });

  callback(state, setState);
  return state;
}

export function useGet<T>(url: string, config: object = {}) {
  return useAxios<T>((state, setState) => {
    useEffect(() => {
      axios
        .get(url, config)
        .then(response => {
          setState({ ...state, data: response.data, loading: false });
        })
        .catch(error => {
          setState({ ...state, error: error.response, loading: false });
        });
    }, [url]);
  });
}

export function usePost<T>(url: string, config: object = {}) {
  return useAxios<T>((state, setState) => {
    useEffect(() => {
      axios
        .post(url, config)
        .then(response => {
          setState({ ...state, data: response.data, loading: false });
        })
        .catch(error => {
          setState({ ...state, error, loading: false });
        });
    }, [url]);
  });
}
