import { createContext } from "react";

export const QueryContext = createContext({
    animeData: [],
    singleData: {},
    query: () => {},
    setData: () => {},
    setSingle: () => {},
});