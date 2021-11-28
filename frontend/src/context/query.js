import { createContext } from "react";

//Creating query context
export const QueryContext = createContext({
    animeData: [],
    singleData: {},
    query: () => {},
    setData: () => {},
    setSingle: () => {},
});