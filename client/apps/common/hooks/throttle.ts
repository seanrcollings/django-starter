import { useEffect, useCallback } from 'react';

export function useThrottledEffect(effect: () => void, timeout: number, deps: any[]) {
  const callback = useCallback(effect, deps);

  useEffect(() => {
    const handler = setTimeout(() => {
      callback();
    }, timeout);

    return () => { clearTimeout(handler); };

  }, [callback, timeout]);
}