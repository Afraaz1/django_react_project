import { createContext } from "react";

export const QueryContext = createContext({
    animeData: [],
    singleData: {},
    search: () => {},
    setData: () => {},
    setSingle: () => {},
});