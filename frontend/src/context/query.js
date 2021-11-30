import { createContext } from "react";

//Creating query context to share methods accross all pages using react compoents
export const QueryContext = createContext({
    animeData: [],
    singleData: {},
    query: () => {},
    setData: () => {},
    setSingle: () => {},
});