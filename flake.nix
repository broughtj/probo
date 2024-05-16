{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let 
        pkgs = nixpkgs.legacyPackages.${system};
	pythonPackages = packages: with packages; [ 
	  bibtexparser
	  jupyter
	  matplotlib
	  numpy
	  pandas
	  scikit-learn
	  scipy
	  tqdm
	];
	in
	  {
	    devShells.default = pkgs.mkShell {
	      packages = with pkgs; [ (python311.withPackages pythonPackages) poetry texliveFull quarto ];
	    };
	  });
}
