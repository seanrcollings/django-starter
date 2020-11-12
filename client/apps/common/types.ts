interface EmbededData {
  user: {
    readonly loggedIn: boolean;
    readonly username: string;
    readonly firstName: string;
    readonly lastName: string;
  };
}

export const embededData: EmbededData = (window as any).DATA;
