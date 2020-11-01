import {
  useState,
  useEffect,
  Dispatch,
  SetStateAction,
  useCallback,
} from "react";
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

function executePost<T>(
  url: string,
  config: object,
  state: AxiosState<T>,
  setState: Dispatch<SetStateAction<AxiosState<T>>>
) {
  axios
    .post(url, config)
    .then(response => {
      setState({ ...state, data: response.data, loading: false });
    })
    .catch(error => {
      setState({ ...state, error: error.response, loading: false });
    });
}

export function usePost<T>(url: string, config: object = {}) {
  const [state, setState] = useState<AxiosState<T>>({
    data: null,
    error: null,
    loading: false,
  });

  const execute = useCallback(() => {
    setState(prevState => ({ ...prevState, loading: true }));
    executePost<T>(url, config, state, setState);
  }, [url, config]);

  return { state, execute };
}
